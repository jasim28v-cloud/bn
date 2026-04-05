// ==================== VIBE - المتغيرات العامة ====================
let currentUser = null;
let currentPostId = null;
let currentChatUser = null;
let currentProfileUser = null;
let selectedMediaFile = null;
let allPostsCache = [];
let currentDisplayCount = 0;
let isLoadingPosts = false;
let hasMorePosts = true;
const POSTS_PER_PAGE = 8;
let scrollListenerAdded = false;
let badWordsList = [];
let readModeActive = false;
let hideLikesActive = false;
let currentImageUrls = [];
let currentImageIndex = 0;

// ==================== دوال مساعدة ====================
function showToast(message, duration = 2000) {
    const toast = document.getElementById('customToast');
    if (!toast) return;
    toast.textContent = message;
    toast.style.opacity = '1';
    setTimeout(() => {
        toast.style.opacity = '0';
    }, duration);
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
    const hashtags = text.match(/#[\w\u0600-\u06FF]+/g) || [];
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

function openImageViewer(images, index) {
    currentImageUrls = images;
    currentImageIndex = index;
    const viewer = document.getElementById('imageViewerModal');
    const viewerImg = document.getElementById('viewerImage');
    if (viewerImg && images[index]) viewerImg.src = images[index];
    viewer.classList.add('open');
}

function closeImageViewer() {
    document.getElementById('imageViewerModal').classList.remove('open');
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

// ==================== Bad Words ====================
async function loadBadWordsList() {
    const snapshot = await db.ref('badWords').once('value');
    const words = snapshot.val();
    badWordsList = words ? Object.values(words) : [];
}

async function addBadWord(word) {
    if (!word.trim()) return;
    await db.ref('badWords').push().set(word.trim().toLowerCase());
    await loadBadWordsList();
    showToast(`✅ تمت إضافة كلمة: ${word}`);
    if (currentUser?.isAdmin) openAdminPanel();
}

async function removeBadWord(wordId, word) {
    await db.ref(`badWords/${wordId}`).remove();
    await loadBadWordsList();
    showToast(`🗑️ تم حذف كلمة: ${word}`);
    if (currentUser?.isAdmin) openAdminPanel();
}

function showAddBadWordModal() {
    const word = prompt('📝 أدخل الكلمة التي تريد منعها:');
    if (word && word.trim()) addBadWord(word.trim());
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
    showToast(readModeActive ? '📖 تم تفعيل وضع القراءة' : '📖 تم إلغاء وضع القراءة');
}

function toggleHideLikes() {
    hideLikesActive = !hideLikesActive;
    const toggle = document.getElementById('hideLikesToggle');
    if (hideLikesActive) {
        toggle.classList.add('active');
        localStorage.setItem('hideLikes', 'true');
    } else {
        toggle.classList.remove('active');
        localStorage.setItem('hideLikes', 'false');
    }
    showToast(hideLikesActive ? '🔒 تم إخفاء عدد الإعجابات' : '🔒 تم إظهار عدد الإعجابات');
    refreshFeedCache();
}

function toggleTheme() {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    const themeIcon = document.getElementById('themeToggle');
    if (themeIcon) {
        if (isDark) {
            themeIcon.classList.remove('fa-adjust');
            themeIcon.classList.add('fa-sun');
        } else {
            themeIcon.classList.remove('fa-sun');
            themeIcon.classList.add('fa-adjust');
        }
    }
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    showToast(isDark ? '🌙 الوضع الليلي' : '☀️ الوضع النهاري');
}

async function toggleDoNotDisturb() {
    const dndToggle = document.getElementById('dndToggle');
    const isDnd = dndToggle.classList.contains('active');
    if (isDnd) {
        dndToggle.classList.remove('active');
        await db.ref(`users/${currentUser.uid}/dnd`).set(false);
        showToast('🔔 تم تفعيل الإشعارات');
    } else {
        dndToggle.classList.add('active');
        await db.ref(`users/${currentUser.uid}/dnd`).set(true);
        showToast('🔕 تم تفعيل عدم الإزعاج');
    }
}

// ==================== تسجيل الخروج ====================
async function logout() {
    try {
        await auth.signOut();
        showToast('👋 تم تسجيل الخروج');
        setTimeout(() => window.location.href = 'auth.html', 1000);
    } catch (error) {
        showToast('❌ حدث خطأ');
    }
}

// ==================== إنشاء منشور ====================
async function createPost() {
    let text = document.getElementById('postText')?.value;
    if (containsBadWords(text)) return showToast('⚠️ المنشور يحتوي على كلمات ممنوعة');
    if (!text && !selectedMediaFile) return showToast('⚠️ الرجاء كتابة نص أو إضافة وسائط');
    text = filterBadWords(text);

    let mediaUrl = "", mediaType = "";
    if (selectedMediaFile) {
        mediaType = selectedMediaFile.type.split('/')[0];
        mediaUrl = await uploadToCloudinary(selectedMediaFile);
        if (!mediaUrl) return;
    }

    const hashtags = extractHashtags(text);
    const postRef = db.ref('posts').push();

    await postRef.set({
        id: postRef.key, userId: currentUser.uid, userName: currentUser.displayName || currentUser.name,
        userAvatar: currentUser.avatar || "", text: text, mediaUrl: mediaUrl, mediaType: mediaType,
        hashtags: hashtags, likes: {}, views: 0, commentsCount: 0, timestamp: Date.now()
    });

    for (const tag of hashtags) {
        await db.ref(`hashtags/${tag.toLowerCase()}/${postRef.key}`).set(true);
    }

    document.getElementById('postText').value = "";
    document.getElementById('mediaPreview').innerHTML = "";
    document.getElementById('mediaPreview').style.display = "none";
    selectedMediaFile = null;
    closeCompose();
    await refreshFeedCache();
    loadTrendingHashtags();
    showToast('✨ تم نشر المنشور بنجاح!');
}

// ==================== حذف منشور ====================
async function deletePost(postId) {
    if (!confirm('⚠️ هل أنت متأكد من حذف هذا المنشور؟')) return;
    const postSnapshot = await db.ref(`posts/${postId}`).once('value');
    const post = postSnapshot.val();
    if (post.userId !== currentUser.uid && !currentUser.isAdmin) return showToast('❌ لا يمكنك حذف منشور ليس لك');
    if (post.hashtags) {
        for (const tag of post.hashtags) {
            await db.ref(`hashtags/${tag.toLowerCase()}/${postId}`).remove();
        }
    }
    await db.ref(`posts/${postId}`).remove();
    await refreshFeedCache();
    loadTrendingHashtags();
    showToast('🗑️ تم حذف المنشور');
}

// ==================== إعجاب ====================
async function likePost(postId) {
    const likeRef = db.ref(`posts/${postId}/likes/${currentUser.uid}`);
    const snapshot = await likeRef.once('value');
    const wasLiked = snapshot.exists();

    if (wasLiked) {
        await likeRef.remove();
    } else {
        await likeRef.set(true);
        const postSnapshot = await db.ref(`posts/${postId}`).once('value');
        const post = postSnapshot.val();
        if (post && post.userId !== currentUser.uid) {
            await db.ref(`notifications/${post.userId}`).push({
                type: 'like', userId: currentUser.uid,
                userName: currentUser.displayName || currentUser.name,
                postId: postId, timestamp: Date.now(), read: false
            });
        }
    }
    refreshFeedCache();
}

// ==================== تعليقات ====================
async function openComments(postId) {
    currentPostId = postId;
    document.getElementById('commentsPanel').classList.add('open');
    await loadComments(postId);
}

function closeComments() {
    document.getElementById('commentsPanel').classList.remove('open');
    currentPostId = null;
}

async function loadComments(postId) {
    const snapshot = await db.ref(`comments/${postId}`).once('value');
    const comments = snapshot.val();
    const container = document.getElementById('commentsList');
    if (!comments) {
        container.innerHTML = '<div style="text-align: center; padding: 20px;">لا توجد تعليقات</div>';
        return;
    }
    let html = '';
    const commentsArray = Object.values(comments).sort((a, b) => b.timestamp - a.timestamp);
    for (const comment of commentsArray) {
        const userSnapshot = await db.ref(`users/${comment.userId}`).once('value');
        const userData = userSnapshot.val();
        const isVerified = userData?.verified || false;
        html += `
            <div class="chat-message">
                <div class="message-bubble">
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                        <span style="font-weight: 600; cursor: pointer;" onclick="openProfile('${comment.userId}')">${escapeHtml(comment.userName)}</span>
                        ${isVerified ? '<i class="fas fa-check-circle verified-badge" style="color: #FFD700; font-size: 12px;"></i>' : ''}
                        <span style="font-size: 10px; color: #8e8e8e;">${formatTime(comment.timestamp)}</span>
                    </div>
                    <div>${escapeHtml(comment.text)}</div>
                </div>
            </div>
        `;
    }
    container.innerHTML = html;
}

async function addComment() {
    let text = document.getElementById('commentInput')?.value;
    if (!text || !currentPostId) return;
    if (containsBadWords(text)) return showToast('⚠️ التعليق يحتوي على كلمات ممنوعة');
    text = filterBadWords(text);

    const commentRef = db.ref(`comments/${currentPostId}`).push();
    await commentRef.set({
        userId: currentUser.uid, userName: currentUser.displayName || currentUser.name,
        text: text, timestamp: Date.now()
    });

    const postRef = db.ref(`posts/${currentPostId}`);
    const snapshot = await postRef.once('value');
    const post = snapshot.val();
    await postRef.update({ commentsCount: (post.commentsCount || 0) + 1 });

    document.getElementById('commentInput').value = '';
    await loadComments(currentPostId);
    refreshFeedCache();
    showToast('💬 تم إضافة التعليق');
}

// ==================== الملف الشخصي ====================
async function openMyProfile() {
    if (currentUser) openProfile(currentUser.uid);
}

async function openProfile(userId) {
    currentProfileUser = userId;
    const snapshot = await db.ref(`users/${userId}`).once('value');
    const userData = snapshot.val();
    if (!userData) return;

    const profileCover = document.getElementById('profileCover');
    if (profileCover) {
        if (userData.cover) profileCover.style.backgroundImage = `url(${userData.cover})`;
        else profileCover.style.backgroundImage = 'linear-gradient(135deg, #ff6b35, #f7b733)';
    }

    const profileAvatarLarge = document.getElementById('profileAvatarLarge');
    profileAvatarLarge.innerHTML = userData.avatar ? `<img src="${userData.avatar}">` : '<i class="fas fa-user text-5xl text-white flex items-center justify-center h-full"></i>';
    document.getElementById('profileName').innerHTML = `${escapeHtml(userData.name)} ${userData.verified ? '<i class="fas fa-check-circle verified-badge" style="color: #FFD700; font-size: 20px;"></i>' : ''}`;
    document.getElementById('profileBio').textContent = userData.bio || "مرحباً! أنا في VIBE ✨";

    const followersSnapshot = await db.ref(`followers/${userId}`).once('value');
    const followingSnapshot = await db.ref(`following/${userId}`).once('value');
    document.getElementById('profileFollowersCount').textContent = followersSnapshot.exists() ? Object.keys(followersSnapshot.val()).length : 0;
    document.getElementById('profileFollowingCount').textContent = followingSnapshot.exists() ? Object.keys(followingSnapshot.val()).length : 0;

    const postsSnapshot = await db.ref('posts').once('value');
    const posts = postsSnapshot.val();
    document.getElementById('profilePostsCount').textContent = posts ? Object.values(posts).filter(p => p.userId === userId).length : 0;

    const buttonsDiv = document.getElementById('profileButtons');
    if (userId !== currentUser.uid) {
        const isFollowing = await checkIfFollowing(userId);
        buttonsDiv.innerHTML = `<button class="profile-btn ${isFollowing ? '' : 'profile-btn-primary'}" onclick="toggleFollow('${userId}')">${isFollowing ? '✅ متابَع' : '➕ متابعة'}</button>
                                <button class="profile-btn" onclick="openChat('${userId}')"><i class="fas fa-comment"></i> راسل</button>`;
        if (currentUser.isAdmin) {
            buttonsDiv.innerHTML += `<button class="profile-btn" onclick="verifyUser('${userId}')">✅ توثيق</button>
                                    <button class="profile-btn" onclick="deleteUser('${userId}')" style="color: red;">🗑️ حذف</button>`;
        }
    } else {
        buttonsDiv.innerHTML = `<button class="profile-btn" onclick="openEditProfileModal()"><i class="fas fa-edit"></i> تعديل</button>
                                <button class="profile-btn" onclick="changeAvatar()"><i class="fas fa-camera"></i> صورة</button>
                                ${currentUser.isAdmin ? '<button class="profile-btn profile-btn-primary" onclick="openAdminPanel()">🔧 لوحة التحكم</button>' : ''}`;
    }

    await loadProfilePosts(userId);
    document.getElementById('profilePanel').classList.add('open');
}

async function checkIfFollowing(userId) {
    const snapshot = await db.ref(`followers/${userId}/${currentUser.uid}`).once('value');
    return snapshot.exists();
}

async function toggleFollow(userId) {
    const isFollowing = await checkIfFollowing(userId);
    if (isFollowing) {
        await db.ref(`followers/${userId}/${currentUser.uid}`).remove();
        await db.ref(`following/${currentUser.uid}/${userId}`).remove();
        showToast('❌ تم إلغاء المتابعة');
    } else {
        await db.ref(`followers/${userId}/${currentUser.uid}`).set(true);
        await db.ref(`following/${currentUser.uid}/${userId}`).set(true);
        showToast('✅ تم المتابعة');
    }
    openProfile(userId);
}

async function loadProfilePosts(userId) {
    const postsSnapshot = await db.ref('posts').once('value');
    const posts = postsSnapshot.val();
    const userPosts = posts ? Object.values(posts).filter(p => p.userId === userId).sort((a, b) => b.timestamp - a.timestamp) : [];
    const grid = document.getElementById('profilePostsGrid');
    if (!grid) return;
    if (userPosts.length === 0) {
        grid.innerHTML = '<div class="text-center p-8 text-gray-500">📭 لا توجد منشورات</div>';
        return;
    }
    let html = '';
    for (const post of userPosts.slice(0, 9)) {
        html += `<div class="grid-item" onclick="openComments('${post.id}')">
                    ${post.mediaUrl ? (post.mediaType === 'image' ? `<img src="${post.mediaUrl}">` : `<video src="${post.mediaUrl}"></video>`) : '<i class="fas fa-file-alt text-2xl"></i>'}
                    <div class="grid-item-overlay"><span><i class="fas fa-heart"></i> ${post.likes ? Object.keys(post.likes).length : 0}</span></div>
                </div>`;
    }
    grid.innerHTML = html;
}

async function loadProfileMedia(userId) {
    const postsSnapshot = await db.ref('posts').once('value');
    const posts = postsSnapshot.val();
    const userPosts = posts ? Object.values(posts).filter(p => p.userId === userId && p.mediaUrl).sort((a, b) => b.timestamp - a.timestamp) : [];
    const grid = document.getElementById('profilePostsGrid');
    if (!grid) return;
    if (userPosts.length === 0) {
        grid.innerHTML = '<div class="text-center p-8 text-gray-500">🎬 لا توجد وسائط</div>';
        return;
    }
    let html = '';
    for (const post of userPosts.slice(0, 9)) {
        html += `<div class="grid-item" onclick="openComments('${post.id}')">
                    ${post.mediaType === 'image' ? `<img src="${post.mediaUrl}">` : `<video src="${post.mediaUrl}"></video>`}
                </div>`;
    }
    grid.innerHTML = html;
}

function openEditProfileModal() {
    document.getElementById('editName').value = currentUser.displayName || currentUser.name || '';
    document.getElementById('editBio').value = currentUser.bio || '';
    document.getElementById('editWebsite').value = currentUser.website || '';
    document.getElementById('editProfileModal').classList.add('open');
}

function closeEditProfileModal() {
    document.getElementById('editProfileModal').classList.remove('open');
}

async function saveProfileEdit() {
    const newName = document.getElementById('editName')?.value;
    const newBio = document.getElementById('editBio')?.value;
    const newWebsite = document.getElementById('editWebsite')?.value;
    if (newName && newName.trim()) await currentUser.updateProfile({ displayName: newName.trim() });
    await db.ref(`users/${currentUser.uid}`).update({ name: newName || currentUser.name, bio: newBio || "", website: newWebsite || "" });
    closeEditProfileModal();
    openProfile(currentUser.uid);
    showToast('💾 تم حفظ التغييرات');
}

async function changeAvatar() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.onchange = async (e) => {
        const file = e.target.files[0];
        if (file) {
            const url = await uploadToCloudinary(file);
            if (url) {
                await db.ref(`users/${currentUser.uid}`).update({ avatar: url });
                currentUser.avatar = url;
                openProfile(currentUser.uid);
                showToast('🖼️ تم تغيير الصورة');
            }
        }
    };
    input.click();
}

// ==================== المحادثات ====================
async function openChat(userId) {
    const snapshot = await db.ref(`users/${userId}`).once('value');
    currentChatUser = snapshot.val();
    document.getElementById('chatUserName').textContent = currentChatUser.name;
    const chatAvatar = document.getElementById('chatAvatar');
    chatAvatar.innerHTML = currentChatUser.avatar ? `<img src="${currentChatUser.avatar}">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>';
    await loadChatMessages(userId);
    document.getElementById('chatPanel').classList.add('open');
}

function closeChat() {
    document.getElementById('chatPanel').classList.remove('open');
    if (currentChatUser) {
        const chatId = getChatId(currentUser.uid, currentChatUser.uid);
        db.ref(`chats/${chatId}`).off();
    }
    currentChatUser = null;
}

function getChatId(user1, user2) {
    return [user1, user2].sort().join('_');
}

async function loadChatMessages(userId) {
    const chatId = getChatId(currentUser.uid, userId);
    db.ref(`chats/${chatId}`).off();
    db.ref(`chats/${chatId}`).on('value', (snapshot) => {
        const messages = snapshot.val();
        const container = document.getElementById('chatMessages');
        if (!container) return;
        if (!messages) {
            container.innerHTML = '<div class="text-center p-4">💬 لا توجد رسائل بعد</div>';
            return;
        }
        let html = '';
        const messagesArray = Object.values(messages).sort((a, b) => a.timestamp - b.timestamp);
        for (const msg of messagesArray) {
            const isSent = msg.senderId === currentUser.uid;
            html += `<div class="chat-message ${isSent ? 'sent' : ''}">
                        <div class="message-bubble ${isSent ? 'sent' : ''}">
                            ${msg.text ? escapeHtml(msg.text) : ''}
                            ${msg.imageUrl ? `<img src="${msg.imageUrl}" class="message-image" style="max-width: 200px; border-radius: 12px; margin-top: 8px; cursor: pointer;" onclick="openImageViewer(['${msg.imageUrl}'], 0)">` : ''}
                        </div>
                    </div>`;
        }
        container.innerHTML = html;
        container.scrollTop = container.scrollHeight;
    });
}

async function sendChatMessage() {
    const input = document.getElementById('chatMessageInput');
    let text = input?.value;
    if (!text || !currentChatUser) return;
    if (containsBadWords(text)) return showToast('⚠️ الرسالة تحتوي على كلمات ممنوعة');
    text = filterBadWords(text);
    const chatId = getChatId(currentUser.uid, currentChatUser.uid);
    await db.ref(`chats/${chatId}`).push({ senderId: currentUser.uid, text: text, timestamp: Date.now(), read: false });
    input.value = '';
}

// ==================== قائمة المحادثات ====================
async function openConversations() {
    const snapshot = await db.ref('chats').once('value');
    const chats = snapshot.val();
    const container = document.getElementById('conversationsList');
    if (!chats) {
        container.innerHTML = '<div class="text-center p-4">💬 لا توجد محادثات</div>';
    } else {
        const conversations = [];
        for (const [chatId, messages] of Object.entries(chats)) {
            const [user1, user2] = chatId.split('_');
            const otherUserId = user1 === currentUser.uid ? user2 : user1;
            const userSnapshot = await db.ref(`users/${otherUserId}`).once('value');
            const userData = userSnapshot.val();
            const messagesArray = Object.values(messages);
            const lastMessage = messagesArray.sort((a, b) => b.timestamp - a.timestamp)[0];
            conversations.push({ userId: otherUserId, userData, lastMessage, timestamp: lastMessage.timestamp });
        }
        conversations.sort((a, b) => b.timestamp - a.timestamp);
        let html = '';
        for (const conv of conversations) {
            html += `<div class="follower-item" onclick="closeConversations(); openChat('${conv.userId}')">
                        <div class="post-avatar" style="width: 48px; height: 48px;">${conv.userData?.avatar ? `<img src="${conv.userData.avatar}">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>'}</div>
                        <div><div style="font-weight: 600;">${escapeHtml(conv.userData?.name || 'مستخدم')}</div>
                        <div style="font-size: 12px;">${conv.lastMessage.text ? conv.lastMessage.text.substring(0, 30) : 'صورة'}</div></div>
                    </div>`;
        }
        container.innerHTML = html;
    }
    document.getElementById('conversationsPanel').classList.add('open');
}

function closeConversations() {
    document.getElementById('conversationsPanel').classList.remove('open');
}

// ==================== الإشعارات ====================
async function loadNotifications() {
    if (!currentUser) return;
    db.ref(`notifications/${currentUser.uid}`).on('value', (snapshot) => {
        const notifications = snapshot.val();
        const notifIcon = document.querySelector('.nav-item:nth-child(4) i');
        if (notifIcon && notifications) {
            const unread = Object.values(notifications).filter(n => !n.read).length;
            const parent = notifIcon.parentElement;
            if (unread > 0 && !parent.querySelector('.badge')) {
                const badge = document.createElement('div');
                badge.className = 'badge';
                badge.style.cssText = 'position: absolute; top: -6px; right: -10px; background: #ff6b35; color: white; font-size: 9px; border-radius: 50%; width: 16px; height: 16px; display: flex; align-items: center; justify-content: center;';
                badge.textContent = unread;
                parent.style.position = 'relative';
                parent.appendChild(badge);
            } else if (unread === 0) {
                const badge = parent.querySelector('.badge');
                if (badge) badge.remove();
            }
        }
    });
}

async function openNotifications() {
    const snapshot = await db.ref(`notifications/${currentUser.uid}`).once('value');
    const notifications = snapshot.val();
    const container = document.getElementById('notificationsList');
    if (!notifications) {
        container.innerHTML = '<div class="text-center p-4">🔔 لا توجد إشعارات</div>';
    } else {
        let html = '';
        const sorted = Object.entries(notifications).sort((a, b) => b[1].timestamp - a[1].timestamp);
        for (const [id, notif] of sorted) {
            let actionText = '';
            if (notif.type === 'like') actionText = 'أعجب بمنشورك';
            else if (notif.type === 'comment') actionText = `علق: ${notif.text?.substring(0, 30)}`;
            html += `<div class="follower-item" onclick="markNotificationRead('${id}'); openComments('${notif.postId}')">
                        <div class="post-avatar" style="width: 44px; height: 44px; background: #ff6b35;"><i class="fas ${notif.type === 'like' ? 'fa-heart' : 'fa-comment'} text-white"></i></div>
                        <div><div style="font-weight: 600;">${escapeHtml(notif.userName)}</div><div>${actionText}</div><div style="font-size: 11px;">${formatTime(notif.timestamp)}</div></div>
                    </div>`;
        }
        container.innerHTML = html;
    }
    document.getElementById('notificationsPanel').classList.add('open');
    const updates = {};
    for (const id of Object.keys(notifications)) {
        updates[`notifications/${currentUser.uid}/${id}/read`] = true;
    }
    await db.ref().update(updates);
}

function closeNotifications() {
    document.getElementById('notificationsPanel').classList.remove('open');
}

async function markNotificationRead(notifId) {
    await db.ref(`notifications/${currentUser.uid}/${notifId}/read`).set(true);
}

// ==================== البحث ====================
function openSearch() {
    document.getElementById('searchPanel').classList.add('open');
}

function closeSearch() {
    document.getElementById('searchPanel').classList.remove('open');
    document.getElementById('searchInput').value = '';
    document.getElementById('searchResults').innerHTML = '';
}

async function searchAll() {
    const query = document.getElementById('searchInput')?.value.toLowerCase();
    if (!query) {
        document.getElementById('searchResults').innerHTML = '';
        return;
    }
    const usersSnapshot = await db.ref('users').once('value');
    const users = usersSnapshot.val();
    const hashtagSnapshot = await db.ref('hashtags').once('value');
    const hashtags = hashtagSnapshot.val();
    let results = [];
    if (users) {
        results.push(...Object.values(users).filter(u => u.name?.toLowerCase().includes(query)).map(u => ({ type: 'user', data: u })));
    }
    if (hashtags) {
        for (const [tag, posts] of Object.entries(hashtags)) {
            if (tag.toLowerCase().includes(query)) results.push({ type: 'hashtag', data: { tag: tag, count: Object.keys(posts).length } });
        }
    }
    let html = '';
    for (const result of results) {
        if (result.type === 'user') {
            html += `<div class="follower-item" onclick="closeSearch(); openProfile('${result.data.uid}')">
                        <div class="post-avatar">${result.data.avatar ? `<img src="${result.data.avatar}">` : '<i class="fas fa-user text-white"></i>'}</div>
                        <div><div style="font-weight: 600;">${escapeHtml(result.data.name)}</div></div>
                    </div>`;
        } else if (result.type === 'hashtag') {
            html += `<div class="follower-item" onclick="closeSearch(); searchHashtag('${result.data.tag}')">
                        <div class="post-avatar" style="background: #ff6b35;"><i class="fas fa-hashtag text-white"></i></div>
                        <div><div style="font-weight: 600; color: #ff6b35;">#${escapeHtml(result.data.tag)}</div><div>${result.data.count} منشور</div></div>
                    </div>`;
        }
    }
    document.getElementById('searchResults').innerHTML = html || '<div class="text-center p-4">🔍 لا توجد نتائج</div>';
}

async function searchHashtag(tag) {
    openSearch();
    document.getElementById('searchInput').value = `#${tag}`;
    await searchAll();
}

// ==================== الترند ====================
async function loadTrendingHashtags() {
    const hashtagSnapshot = await db.ref('hashtags').once('value');
    const hashtags = hashtagSnapshot.val();
    if (!hashtags) return;
    const trending = [];
    for (const [tag, posts] of Object.entries(hashtags)) {
        trending.push({ tag, count: Object.keys(posts).length });
    }
    trending.sort((a, b) => b.count - a.count);
    const top5 = trending.slice(0, 5);
    const container = document.getElementById('trendingList');
    if (container) {
        container.innerHTML = top5.map((item, index) => `
            <div class="trending-item" onclick="searchHashtag('${item.tag}')">
                <div class="trending-hashtag">#${escapeHtml(item.tag)}</div>
                <div style="font-size: 11px;">${item.count} منشور</div>
            </div>
        `).join('');
    }
}

// ==================== Infinite Scroll ====================
async function loadAllPostsToCache() {
    const feedContainer = document.getElementById('feedContainer');
    if (!feedContainer) return;

    feedContainer.innerHTML = '<div class="loading"><div class="spinner"></div><span>جاري التحميل...</span></div>';

    const snapshot = await db.ref('posts').once('value');
    const posts = snapshot.val();

    if (!posts || Object.keys(posts).length === 0) {
        feedContainer.innerHTML = '<div class="text-center p-8">✨ لا توجد منشورات بعد - كن أول من ينشر! ✨</div>';
        hasMorePosts = false;
        return;
    }

    let postsArray = Object.values(posts).sort((a, b) => b.timestamp - a.timestamp);

    if (currentUser) {
        const blockedSnapshot = await db.ref(`users/${currentUser.uid}/blockedUsers`).once('value');
        const blockedUsers = blockedSnapshot.val() || {};
        postsArray = postsArray.filter(post => !blockedUsers[post.userId]);
    }

    allPostsCache = postsArray;
    hasMorePosts = allPostsCache.length > POSTS_PER_PAGE;
    currentDisplayCount = POSTS_PER_PAGE;

    feedContainer.innerHTML = '';
    await displayPosts(0, POSTS_PER_PAGE);

    if (!scrollListenerAdded) {
        setupScrollListener();
        scrollListenerAdded = true;
    }
}

async function displayPosts(startIndex, count) {
    const feedContainer = document.getElementById('feedContainer');
    if (!feedContainer) return;

    const endIndex = Math.min(startIndex + count, allPostsCache.length);
    const postsToShow = allPostsCache.slice(startIndex, endIndex);

    for (const post of postsToShow) {
        const userInfoSnapshot = await db.ref(`users/${post.userId}`).once('value');
        const userInfo = userInfoSnapshot.val();
        const isUserVerified = userInfo?.verified || false;
        const isLiked = post.likes && post.likes[currentUser?.uid];
        const likesCount = post.likes ? Object.keys(post.likes).length : 0;
        const isOwner = post.userId === currentUser?.uid;

        let formattedText = escapeHtml(post.text);
        if (post.hashtags) {
            post.hashtags.forEach(tag => {
                const regex = new RegExp(`#${tag}`, 'gi');
                formattedText = formattedText.replace(regex, `<span class="post-hashtags" onclick="searchHashtag('${tag}')">#${tag}</span>`);
            });
        }

        let mediaHtml = '';
        if (post.mediaUrl) {
            if (post.mediaType === 'image') {
                mediaHtml = `<img src="${post.mediaUrl}" class="post-image" loading="lazy" onclick="event.stopPropagation(); openImageViewer(['${post.mediaUrl}'], 0)">`;
            } else if (post.mediaType === 'video') {
                mediaHtml = `<video src="${post.mediaUrl}" class="post-image" controls preload="metadata"></video>`;
            }
        }

        const postHtml = `
            <div class="post-card" data-post-id="${post.id}" ondblclick="likePost('${post.id}')">
                <div class="post-header">
                    <div class="post-user-info" onclick="openProfile('${post.userId}')">
                        <div class="post-avatar">${post.userAvatar ? `<img src="${post.userAvatar}">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>'}</div>
                        <div>
                            <div class="post-username">
                                ${escapeHtml(post.userName)}
                                ${isUserVerified ? '<i class="fas fa-check-circle verified-badge" style="color: #FFD700; font-size: 14px;"></i>' : ''}
                            </div>
                            <div class="post-time">${formatTime(post.timestamp)}</div>
                        </div>
                    </div>
                    <div style="display: flex; gap: 12px;">
                        ${(isOwner || currentUser?.isAdmin) ? `<button class="post-menu" onclick="event.stopPropagation(); deletePost('${post.id}')"><i class="fas fa-trash-alt"></i></button>` : ''}
                        <button class="post-menu" onclick="event.stopPropagation(); openReportModal('${post.id}')"><i class="fas fa-flag"></i></button>
                    </div>
                </div>
                ${mediaHtml}
                <div class="post-actions">
                    <button class="post-action ${isLiked ? 'active' : ''}" onclick="likePost('${post.id}')"><i class="fas fa-heart"></i></button>
                    <button class="post-action" onclick="openComments('${post.id}')"><i class="fas fa-comment"></i></button>
                    <button class="post-action" onclick="sharePost('${post.id}')"><i class="fas fa-paper-plane"></i></button>
                </div>
                ${likesCount > 0 && !hideLikesActive ? `<div class="post-likes">❤️ ${likesCount} إعجاب</div>` : ''}
                <div class="post-caption"><span onclick="openProfile('${post.userId}')">${escapeHtml(post.userName)}</span> ${formattedText}</div>
                ${post.commentsCount > 0 ? `<div class="post-comments" onclick="openComments('${post.id}')">💬 ${post.commentsCount} تعليق</div>` : ''}
                <div class="post-views"><i class="far fa-eye"></i> ${post.views || 0} مشاهدة</div>
            </div>
        `;

        feedContainer.insertAdjacentHTML('beforeend', postHtml);
    }

    if (hasMorePosts && endIndex < allPostsCache.length) {
        let loadMoreDiv = document.getElementById('loadMoreTrigger');
        if (!loadMoreDiv) {
            loadMoreDiv = document.createElement('div');
            loadMoreDiv.id = 'loadMoreTrigger';
            loadMoreDiv.className = 'load-more-btn';
            loadMoreDiv.innerHTML = '<div class="spinner" style="width: 24px; height: 24px;"></div><span>جاري تحميل المزيد...</span>';
            loadMoreDiv.style.display = 'none';
            feedContainer.appendChild(loadMoreDiv);
        }
    } else if (allPostsCache.length > 0 && endIndex >= allPostsCache.length) {
        const loadMoreDiv = document.getElementById('loadMoreTrigger');
        if (loadMoreDiv) loadMoreDiv.remove();
        const endMessage = document.createElement('div');
        endMessage.className = 'text-center p-4';
        endMessage.innerHTML = '✨ لقد وصلت إلى النهاية ✨';
        feedContainer.appendChild(endMessage);
    }
}

async function loadMorePosts() {
    if (isLoadingPosts || !hasMorePosts) return;

    isLoadingPosts = true;
    const loadMoreDiv = document.getElementById('loadMoreTrigger');
    if (loadMoreDiv) loadMoreDiv.style.display = 'flex';

    await new Promise(resolve => setTimeout(resolve, 200));

    const startIndex = currentDisplayCount;
    const newEndIndex = Math.min(startIndex + POSTS_PER_PAGE, allPostsCache.length);

    if (startIndex < allPostsCache.length) {
        await displayPosts(startIndex, POSTS_PER_PAGE);
        currentDisplayCount = newEndIndex;
        hasMorePosts = currentDisplayCount < allPostsCache.length;
    } else {
        hasMorePosts = false;
    }

    if (loadMoreDiv) loadMoreDiv.style.display = 'none';
    isLoadingPosts = false;
}

function setupScrollListener() {
    const handleScroll = () => {
        if (isLoadingPosts || !hasMorePosts) return;
        const scrollPosition = window.innerHeight + window.scrollY;
        const threshold = document.body.offsetHeight - 400;
        if (scrollPosition >= threshold) loadMorePosts();
    };
    window.removeEventListener('scroll', handleScroll);
    window.addEventListener('scroll', handleScroll);
}

async function refreshFeedCache() {
    if (!currentUser) return;

    const snapshot = await db.ref('posts').once('value');
    const posts = snapshot.val();

    if (!posts || Object.keys(posts).length === 0) {
        allPostsCache = [];
        hasMorePosts = false;
        currentDisplayCount = 0;
        const feedContainer = document.getElementById('feedContainer');
        if (feedContainer) feedContainer.innerHTML = '<div class="text-center p-8">✨ لا توجد منشورات بعد - كن أول من ينشر! ✨</div>';
        return;
    }

    let postsArray = Object.values(posts).sort((a, b) => b.timestamp - a.timestamp);

    const blockedSnapshot = await db.ref(`users/${currentUser.uid}/blockedUsers`).once('value');
    const blockedUsers = blockedSnapshot.val() || {};
    postsArray = postsArray.filter(post => !blockedUsers[post.userId]);

    allPostsCache = postsArray;
    hasMorePosts = allPostsCache.length > POSTS_PER_PAGE;
    currentDisplayCount = Math.min(POSTS_PER_PAGE, allPostsCache.length);

    const feedContainer = document.getElementById('feedContainer');
    if (feedContainer) {
        feedContainer.innerHTML = '';
        await displayPosts(0, currentDisplayCount);
    }
}

function resetInfiniteScroll() {
    isLoadingPosts = false;
    hasMorePosts = true;
    allPostsCache = [];
    currentDisplayCount = 0;
}

async function loadFeed() {
    await loadAllPostsToCache();
}

// ==================== مشاركة ====================
async function sharePost(postId) {
    const url = `${window.location.origin}?post=${postId}`;
    navigator.clipboard.writeText(url);
    showToast('🔗 تم نسخ رابط المنشور');
}

// ==================== إبلاغ ====================
function openReportModal(postId) {
    currentReportPostId = postId;
    document.getElementById('reportModal').classList.add('open');
}

function closeReportModal() {
    document.getElementById('reportModal').classList.remove('open');
    currentReportPostId = null;
    selectedReportReason = null;
}

function selectReportReason(element, reason) {
    document.querySelectorAll('.report-reason').forEach(el => el.classList.remove('selected'));
    element.classList.add('selected');
    selectedReportReason = reason;
}

async function submitReport() {
    if (!selectedReportReason || !currentReportPostId) return showToast('⚠️ الرجاء اختيار سبب الإبلاغ');
    await db.ref(`reports/${currentReportPostId}`).push({
        reporterId: currentUser.uid, reporterName: currentUser.displayName || currentUser.name,
        reason: selectedReportReason, timestamp: Date.now()
    });
    showToast('📢 تم إرسال البلاغ، شكراً لك');
    closeReportModal();
}

// ==================== قائمة المتابعين ====================
async function openFollowersList(type) {
    const refPath = type === 'followers' ? `followers/${currentProfileUser}` : `following/${currentProfileUser}`;
    const snapshot = await db.ref(refPath).once('value');
    const data = snapshot.val();
    const container = document.getElementById('followersList');
    if (!data) {
        container.innerHTML = '<div class="text-center p-4">👥 لا يوجد متابعون</div>';
    } else {
        let html = '';
        for (const [userId] of Object.entries(data)) {
            const userSnapshot = await db.ref(`users/${userId}`).once('value');
            const userData = userSnapshot.val();
            html += `<div class="follower-item" onclick="closeFollowers(); openProfile('${userId}')">
                        <div class="post-avatar" style="width: 48px; height: 48px;">${userData?.avatar ? `<img src="${userData.avatar}">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>'}</div>
                        <div><div style="font-weight: 600;">${escapeHtml(userData?.name || 'مستخدم')}</div></div>
                    </div>`;
        }
        container.innerHTML = html;
    }
    document.getElementById('followersPanel').classList.add('open');
}

function closeFollowers() {
    document.getElementById('followersPanel').classList.remove('open');
}

// ==================== لوحة التحكم ====================
async function openAdminPanel() {
    if (!currentUser.isAdmin && currentUser.email !== ADMIN_EMAIL) return showToast('🚫 غير مصرح لك');
    showToast('🔧 جاري تحميل لوحة التحكم...');

    const badWordsSnapshot = await db.ref('badWords').once('value');
    const badWords = badWordsSnapshot.val();
    const badWordsContainer = document.getElementById('adminBadWordsList');
    if (badWordsContainer) {
        if (!badWords) {
            badWordsContainer.innerHTML = '<div class="text-center p-4">📝 لا توجد كلمات ممنوعة</div>';
        } else {
            let html = '';
            for (const [id, word] of Object.entries(badWords)) {
                html += `<div class="admin-item"><div>🚫 ${escapeHtml(word)}</div><button class="admin-delete-btn" onclick="removeBadWord('${id}', '${word}')">حذف</button></div>`;
            }
            badWordsContainer.innerHTML = html;
        }
    }

    const usersSnapshot = await db.ref('users').once('value');
    const postsSnapshot = await db.ref('posts').once('value');
    const commentsSnapshot = await db.ref('comments').once('value');
    const usersCount = usersSnapshot.exists() ? Object.keys(usersSnapshot.val()).length : 0;
    const postsCount = postsSnapshot.exists() ? Object.keys(postsSnapshot.val()).length : 0;
    let commentsCount = 0;
    if (commentsSnapshot.exists()) {
        for (const pc of Object.values(commentsSnapshot.val())) commentsCount += Object.keys(pc).length;
    }
    const verifiedCount = usersSnapshot.exists() ? Object.values(usersSnapshot.val()).filter(u => u.verified).length : 0;

    document.getElementById('adminUsersCount').textContent = usersCount;
    document.getElementById('adminPostsCount').textContent = postsCount;
    document.getElementById('adminCommentsCount').textContent = commentsCount;
    document.getElementById('adminVerifiedCount').textContent = verifiedCount;

    let usersHtml = '';
    if (usersSnapshot.exists()) {
        for (const [uid, user] of Object.entries(usersSnapshot.val())) {
            if (uid !== currentUser.uid) {
                usersHtml += `<div class="admin-item">
                                <div><div class="admin-item-name">${escapeHtml(user.name)}</div><div class="admin-item-email">${escapeHtml(user.email)}</div></div>
                                <div>
                                    ${!user.verified ? `<button class="admin-verify-btn" onclick="verifyUser('${uid}')">✅ توثيق</button>` : '<span style="color: #FFD700;">⭐ موثق</span>'}
                                    <button class="admin-delete-btn" onclick="deleteUser('${uid}')">🗑️ حذف</button>
                                </div>
                            </div>`;
            }
        }
    }
    document.getElementById('adminUsersList').innerHTML = usersHtml || '<div class="text-center p-4">👥 لا يوجد مستخدمين</div>';

    let postsHtml = '';
    if (postsSnapshot.exists()) {
        for (const post of Object.values(postsSnapshot.val()).sort((a, b) => b.timestamp - a.timestamp).slice(0, 20)) {
            postsHtml += `<div class="admin-item"><div><div class="admin-item-name">${escapeHtml(post.userName)}</div><div class="admin-item-email">${escapeHtml(post.text?.substring(0, 50) || '')}</div></div><button class="admin-delete-btn" onclick="deletePost('${post.id}')">🗑️ حذف</button></div>`;
        }
    }
    document.getElementById('adminPostsList').innerHTML = postsHtml || '<div class="text-center p-4">📭 لا توجد منشورات</div>';
    document.getElementById('adminPanel').classList.add('open');
}

function closeAdmin() {
    document.getElementById('adminPanel').classList.remove('open');
}

async function verifyUser(userId) {
    await db.ref(`users/${userId}`).update({ verified: true });
    showToast('✅ تم توثيق المستخدم بنجاح');
    if (currentProfileUser === userId) openProfile(userId);
    refreshFeedCache();
    openAdminPanel();
}

async function deleteUser(userId) {
    if (confirm('⚠️ هل أنت متأكد من حذف هذا المستخدم نهائياً؟')) {
        await db.ref(`users/${userId}`).remove();
        showToast('🗑️ تم حذف المستخدم');
        openAdminPanel();
        refreshFeedCache();
    }
}

// ==================== دوال الإغلاق ====================
function closeCompose() {
    document.getElementById('composeModal').classList.remove('open');
    document.getElementById('postText').value = '';
    document.getElementById('mediaPreview').innerHTML = '';
    document.getElementById('mediaPreview').style.display = 'none';
    selectedMediaFile = null;
}

function openCompose() {
    document.getElementById('composeModal').classList.add('open');
}

function closeProfile() {
    document.getElementById('profilePanel').classList.remove('open');
}

function goToHome() {
    refreshFeedCache();
}

function switchTab(tab) {
    if (tab === 'home') refreshFeedCache();
}

function previewMedia(input, type) {
    const file = input.files[0];
    if (file) {
        selectedMediaFile = file;
        const preview = document.getElementById('mediaPreview');
        const reader = new FileReader();
        reader.onload = function(e) {
            if (type === 'image') preview.innerHTML = `<img src="${e.target.result}" style="max-height: 250px; width: 100%; object-fit: cover;">`;
            else if (type === 'video') preview.innerHTML = `<video src="${e.target.result}" controls style="max-height: 250px; width: 100%;"></video>`;
            preview.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
}

// ==================== حفظ المنشورات ====================
async function savePost(postId) {
    const saveRef = db.ref(`savedPosts/${currentUser.uid}/${postId}`);
    const snapshot = await saveRef.once('value');
    if (snapshot.exists()) {
        await saveRef.remove();
        showToast('📌 تم إزالة من المحفوظات');
    } else {
        await saveRef.set(true);
        showToast('💾 تم حفظ المنشور');
    }
}

async function openSavedPosts() {
    const snapshot = await db.ref(`savedPosts/${currentUser.uid}`).once('value');
    const savedPosts = snapshot.val();
    const container = document.getElementById('savedPostsGrid');
    if (!savedPosts) {
        container.innerHTML = '<div class="text-center p-8" style="grid-column: span 3;">📭 لا توجد منشورات محفوظة</div>';
    } else {
        let html = '';
        for (const postId of Object.keys(savedPosts)) {
            const postSnapshot = await db.ref(`posts/${postId}`).once('value');
            const post = postSnapshot.val();
            if (post) {
                html += `<div class="grid-item" onclick="openComments('${postId}')">
                            ${post.mediaUrl ? (post.mediaType === 'image' ? `<img src="${post.mediaUrl}">` : `<video src="${post.mediaUrl}"></video>`) : '<i class="fas fa-file-alt text-2xl"></i>'}
                        </div>`;
            }
        }
        container.innerHTML = html || '<div class="text-center p-8" style="grid-column: span 3;">📭 لا توجد منشورات محفوظة</div>';
    }
    document.getElementById('savedPostsPanel').classList.add('open');
}

function closeSavedPosts() {
    document.getElementById('savedPostsPanel').classList.remove('open');
}

// ==================== تحديث آخر ظهور ====================
setInterval(async () => {
    if (currentUser) await db.ref(`users/${currentUser.uid}/lastSeen`).set(Date.now());
}, 60000);

// ==================== مراقبة حالة المستخدم ====================
const initLoader = document.getElementById('initLoader');

auth.onAuthStateChanged(async (user) => {
    if (initLoader) {
        setTimeout(() => {
            initLoader.style.opacity = '0';
            setTimeout(() => {
                if (initLoader) initLoader.style.display = 'none';
            }, 300);
        }, 500);
    }

    if (user) {
        currentUser = user;
        const snapshot = await db.ref(`users/${user.uid}`).once('value');
        if (snapshot.exists()) {
            currentUser = { ...currentUser, ...snapshot.val() };
        } else {
            await db.ref(`users/${user.uid}`).set({
                name: user.displayName || user.email.split('@')[0],
                email: user.email,
                bio: "مرحباً! أنا في VIBE ✨",
                avatar: "", cover: "", website: "",
                verified: false, isAdmin: user.email === ADMIN_EMAIL,
                blockedUsers: {}, mutedUntil: 0, createdAt: Date.now()
            });
            currentUser.isAdmin = user.email === ADMIN_EMAIL;
        }
        document.getElementById('mainApp').style.display = 'block';

        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark') document.body.classList.add('dark-mode');
        const savedReadMode = localStorage.getItem('readMode');
        if (savedReadMode === 'true') {
            readModeActive = true;
            document.getElementById('readModeToggle')?.classList.add('active');
        }
        const savedHideLikes = localStorage.getItem('hideLikes');
        if (savedHideLikes === 'true') {
            hideLikesActive = true;
            document.getElementById('hideLikesToggle')?.classList.add('active');
        }

        await loadBadWordsList();
        resetInfiniteScroll();
        await loadFeed();
        loadNotifications();
        loadTrendingHashtags();
    } else {
        window.location.href = 'auth.html';
    }
});
