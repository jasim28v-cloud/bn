// 💖 VIBE 2026 - Premium Pink Glass Edition
// ==================== المتغيرات العامة ====================
let currentUser = null;
let currentPostId = null;
let currentChatUser = null;
let currentProfileUser = null;
let selectedMediaFile = null;
let mediaRecorder = null;
let audioChunks = [];
let isRecording = false;
let typingTimeout = null;
let currentReportPostId = null;
let selectedReportReason = null;
let readModeActive = false;
let hideLikesActive = false;
let currentImageUrls = [];
let currentImageIndex = 0;

let allPostsCache = [];
let currentDisplayCount = 0;
let isLoadingPosts = false;
let hasMorePosts = true;
const POSTS_PER_PAGE = 8;
let scrollListenerAdded = false;

let agoraClient = null;
let localTracks = { videoTrack: null, audioTrack: null };
let isCallActive = false;
let badWordsList = [];

// ==================== دوال مساعدة ====================
function showToast(message, duration = 2000) {
    const toast = document.getElementById('customToast');
    if (!toast) return;
    toast.textContent = message;
    toast.style.opacity = '1';
    setTimeout(() => { toast.style.opacity = '0'; }, duration);
}

function openImageViewer(images, index) {
    currentImageUrls = images;
    currentImageIndex = index;
    const viewer = document.getElementById('imageViewerModal');
    const viewerImg = document.getElementById('viewerImage');
    if (viewerImg && images[index]) viewerImg.src = images[index];
    viewer.classList.add('open');
}

function closeImageViewer() { document.getElementById('imageViewerModal').classList.remove('open'); }

function prevImage() {
    if (currentImageIndex > 0) {
        currentImageIndex--;
        document.getElementById('viewerImage').src = currentImageUrls[currentImageIndex];
    }
}

function nextImage() {
    if (currentImageIndex < currentImageUrls.length - 1) {
        currentImageIndex++;
        document.getElementById('viewerImage').src = currentImageUrls[currentImageIndex];
    }
}

function formatTime(timestamp) {
    const now = Date.now();
    const diff = now - timestamp;
    const seconds = Math.floor(diff / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);
    if (days > 0) return `${days} يوم`;
    if (hours > 0) return `${hours} ساعة`;
    if (minutes > 0) return `${minutes} دقيقة`;
    return `${seconds} ثانية`;
}

function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function extractHashtags(text) {
    const hashtags = text.match(/#[\w؀-ۿ]+/g) || [];
    return hashtags.map(tag => tag.substring(1));
}

function containsBadWords(text) {
    if (!text || badWordsList.length === 0) return false;
    const lowerText = text.toLowerCase();
    for (const word of badWordsList) {
        if (lowerText.includes(word.toLowerCase())) return true;
    }
    return false;
}

function filterBadWords(text) {
    if (!text || badWordsList.length === 0) return text;
    let filtered = text;
    for (const word of badWordsList) {
        const regex = new RegExp(word, 'gi');
        filtered = filtered.replace(regex, '*'.repeat(word.length));
    }
    return filtered;
}

// 💎 Verified Badge HTML Generator
function getVerifiedBadge(size = 'main') {
    return `<span class="verified-badge-${size}"><i class="fas fa-check"></i></span>`;
}

// ==================== رفع الملفات ====================
async function uploadToCloudinary(file) {
    const url = `https://api.cloudinary.com/v1_1/${CLOUD_NAME}/upload`;
    const formData = new FormData();
    formData.append('file', file);
    formData.append('upload_preset', UPLOAD_PRESET);
    try {
        const response = await fetch(url, { method: 'POST', body: formData });
        const data = await response.json();
        if (data.secure_url) return data.secure_url;
        throw new Error('Upload failed');
    } catch (error) {
        console.error('Cloudinary error:', error);
        showToast('فشل رفع الملف');
        return null;
    }
}

// ==================== الإعدادات ====================
function toggleReadMode() {
    readModeActive = !readModeActive;
    const toggle = document.getElementById('readModeToggle');
    if (readModeActive) {
        document.body.classList.add('read-mode');
        toggle.classList.add('active');
        localStorage.setItem('readMode', 'true');
    } else {
        document.body.classList.remove('read-mode');
        toggle.classList.remove('active');
        localStorage.setItem('readMode', 'false');
    }
    showToast(readModeActive ? 'تم تفعيل وضع القراءة' : 'تم إلغاء وضع القراءة');
}

function toggleHideLikes() {
    hideLikesActive = !hideLikesActive;
    const toggle = document.getElementById('hideLikesToggle');
    if (hideLikesActive) { toggle.classList.add('active'); localStorage.setItem('hideLikes', 'true'); }
    else { toggle.classList.remove('active'); localStorage.setItem('hideLikes', 'false'); }
    showToast(hideLikesActive ? 'تم إخفاء عدد الإعجابات' : 'تم إظهار عدد الإعجابات');
    refreshFeedCache();
}

function toggleTheme() {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    const themeIcon = document.getElementById('themeToggle');
    if (themeIcon) {
        if (isDark) { themeIcon.classList.remove('fa-adjust'); themeIcon.classList.add('fa-sun'); }
        else { themeIcon.classList.remove('fa-sun'); themeIcon.classList.add('fa-adjust'); }
    }
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    showToast(isDark ? '🌙 الوضع الليلي' : '☀️ الوضع النهاري');
}

async function toggleDoNotDisturb() {
    const dndToggle = document.getElementById('dndToggle');
    const isDnd = dndToggle.classList.contains('active');
    if (isDnd) { dndToggle.classList.remove('active'); await db.ref(`users/${currentUser.uid}/dnd`).set(false); showToast('تم تفعيل الإشعارات'); }
    else { dndToggle.classList.add('active'); await db.ref(`users/${currentUser.uid}/dnd`).set(true); showToast('تم تفعيل عدم الإزعاج'); }
}

async function loadDndStatus() {
    const snapshot = await db.ref(`users/${currentUser.uid}/dnd`).once('value');
    const isDnd = snapshot.val();
    const dndToggle = document.getElementById('dndToggle');
    if (isDnd && dndToggle) dndToggle.classList.add('active');
    else if (dndToggle) dndToggle.classList.remove('active');
}

// ==================== تسجيل الخروج ====================
async function logout() {
    try {
        await auth.signOut();
        localStorage.removeItem('auth_logged_in');
        showToast('تم تسجيل الخروج بنجاح');
        setTimeout(() => { window.location.href = 'auth.html'; }, 1000);
    } catch (error) {
        console.error('Logout error:', error);
        showToast('حدث خطأ أثناء تسجيل الخروج');
    }
}

// ==================== تغيير الصورة والغلاف ====================
async function changeAvatar() {
    const input = document.createElement('input');
    input.type = 'file'; input.accept = 'image/*';
    input.onchange = async (e) => {
        const file = e.target.files[0];
        if (file) {
            const url = await uploadToCloudinary(file);
            if (url) {
                await db.ref(`users/${currentUser.uid}`).update({ avatar: url });
                currentUser.avatar = url;
                if (currentProfileUser) openProfile(currentProfileUser);
                else openProfile(currentUser.uid);
                showToast('تم تغيير الصورة الشخصية 💖');
            }
        }
    };
    input.click();
}

async function changeCover() {
    const input = document.createElement('input');
    input.type = 'file'; input.accept = 'image/*';
    input.onchange = async (e) => {
        const file = e.target.files[0];
        if (file) {
            const url = await uploadToCloudinary(file);
            if (url) {
                await db.ref(`users/${currentUser.uid}`).update({ cover: url });
                currentUser.cover = url;
                if (currentProfileUser) openProfile(currentProfileUser);
                else openProfile(currentUser.uid);
                showToast('تم تغيير صورة الغلاف 💖');
            }
        }
    };
    input.click();
}

// ==================== دوال الإغلاق والواجهات ====================
function closeCompose() { document.getElementById('composeModal').classList.remove('open'); document.getElementById('postText').value = ''; document.getElementById('mediaPreview').innerHTML = ''; document.getElementById('mediaPreview').style.display = 'none'; document.getElementById('pollBuilder').style.display = 'none'; document.getElementById('schedulePicker').style.display = 'none'; selectedMediaFile = null; }
function openCompose() { document.getElementById('composeModal').classList.add('open'); }
function closeComments() { document.getElementById('commentsPanel').classList.remove('open'); currentPostId = null; }
function closeProfile() { document.getElementById('profilePanel').classList.remove('open'); }
function closeNotifications() { document.getElementById('notificationsPanel').classList.remove('open'); }
function closeSearch() { document.getElementById('searchPanel').classList.remove('open'); document.getElementById('searchInput').value = ''; document.getElementById('searchResults').innerHTML = ''; }
function openSearch() { document.getElementById('searchPanel').classList.add('open'); }
function goToHome() { refreshFeedCache(); }
function switchTab(tab) { if (tab === 'home') refreshFeedCache(); }

function previewMedia(input, type) {
    const file = input.files[0];
    if (file) {
        selectedMediaFile = file;
        const preview = document.getElementById('mediaPreview');
        const reader = new FileReader();
        reader.onload = function(e) {
            if (type === 'image') preview.innerHTML = `<img src="${e.target.result}">`;
            else preview.innerHTML = `<video src="${e.target.result}" controls></video>`;
            preview.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
}

// ==================== الترند ====================
async function loadTrendingHashtags() {
    const hashtagSnapshot = await db.ref('hashtags').once('value');
    const hashtags = hashtagSnapshot.val();
    if (!hashtags) return;
    const trending = [];
    for (const [tag, posts] of Object.entries(hashtags)) { trending.push({ tag, count: Object.keys(posts).length }); }
    trending.sort((a, b) => b.count - a.count);
    const top5 = trending.slice(0, 5);
    const container = document.getElementById('trendingList');
    if (container) {
        container.innerHTML = top5.map((item, index) => `
            <div class="trending-item" onclick="searchHashtag('${item.tag}')">
                <div style="font-weight: 600; color: var(--pink);">#${escapeHtml(item.tag)}</div>
                <div style="font-size: 12px; color: #8e8e8e;">${item.count} منشور</div>
            </div>
        `).join('');
    }
}

// ==================== تحديث آخر ظهور ====================
setInterval(async () => { if (currentUser) await db.ref(`users/${currentUser.uid}/lastSeen`).set(Date.now()); }, 60000);

// ==================== المصادقة ====================
const initLoader = document.getElementById('initLoader');

auth.onAuthStateChanged(async (user) => {
    if (initLoader) { setTimeout(() => { initLoader.style.opacity = '0'; setTimeout(() => { if (initLoader) initLoader.style.display = 'none'; }, 300); }, 500); }
    
    if (user) {
        currentUser = user;
        const snapshot = await db.ref(`users/${user.uid}`).once('value');
        if (snapshot.exists()) { currentUser = { ...currentUser, ...snapshot.val() }; }
        else {
            await db.ref(`users/${user.uid}`).set({
                uid: user.uid, name: user.displayName || user.email.split('@')[0],
                email: user.email, bio: "مرحباً! أنا في VIBE ✨", avatar: "", cover: "",
                website: "", verified: false, isAdmin: user.email === ADMIN_EMAIL,
                blockedUsers: {}, mutedUntil: 0, createdAt: Date.now()
            });
            currentUser.isAdmin = user.email === ADMIN_EMAIL;
        }
        document.getElementById('mainApp').style.display = 'block';
        
        const st = localStorage.getItem('theme');
        if (st === 'dark') document.body.classList.add('dark-mode');
        const srm = localStorage.getItem('readMode');
        if (srm === 'true') { readModeActive = true; document.getElementById('readModeToggle')?.classList.add('active'); }
        const shl = localStorage.getItem('hideLikes');
        if (shl === 'true') { hideLikesActive = true; document.getElementById('hideLikesToggle')?.classList.add('active'); }
        
        await loadBadWordsList();
        resetInfiniteScroll();
        await loadFeed();
        loadNotifications();
        loadTrendingHashtags();
        loadDndStatus();
        checkScheduledPosts();
    } else {
        window.location.href = 'auth.html';
    }
});

console.log('💖 VIBE 2026 - Premium Pink Glass Ready!');
