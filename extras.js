// 💖 VIBE 2026 - Extras Module (Search, Notifications, Reports, Saved)

// ==================== البحث ====================
async function searchUser(username) { openSearch(); document.getElementById('searchInput').value = username; await searchAll(); }
async function searchHashtag(tag) { openSearch(); document.getElementById('searchInput').value = `#${tag}`; await searchAll(); }

async function searchAll() {
    const query = document.getElementById('searchInput')?.value.toLowerCase();
    if (!query) { document.getElementById('searchResults').innerHTML = ''; return; }
    const usersSnapshot = await db.ref('users').once('value');
    const users = usersSnapshot.val();
    const hashtagSnapshot = await db.ref('hashtags').once('value');
    const hashtags = hashtagSnapshot.val();
    let results = [];
    if (users) results.push(...Object.values(users).filter(u => u.name?.toLowerCase().includes(query) || u.email?.toLowerCase().includes(query)).map(u => ({ type: 'user', data: u })));
    if (hashtags && query.startsWith('#')) {
        const tag = query.substring(1);
        if (hashtags[tag]) results.push({ type: 'hashtag', data: { tag, count: Object.keys(hashtags[tag]).length } });
    } else if (hashtags) {
        for (const [tag, posts] of Object.entries(hashtags)) { if (tag.toLowerCase().includes(query)) results.push({ type: 'hashtag', data: { tag, count: Object.keys(posts).length } }); }
    }
    let html = '';
    for (const r of results) {
        if (r.type === 'user') {
            // 💎 Verified Badge in Search
            const vBadge = r.data.verified ? getVerifiedBadge('sm') : '';
            html += `<div class="follower-item" onclick="closeSearch(); openProfile('${r.data.uid}')"><div class="post-avatar" style="width: 44px; height: 44px;">${r.data.avatar ? `<img src="${r.data.avatar}">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>'}</div><div><div style="font-weight: 600;">${vBadge}${escapeHtml(r.data.name)}</div><div style="font-size: 12px; color: #8e8e8e;">${escapeHtml(r.data.email)}</div></div></div>`;
        }
        else if (r.type === 'hashtag') html += `<div class="follower-item" onclick="closeSearch(); searchHashtag('${r.data.tag}')"><div class="post-avatar" style="width: 44px; height: 44px; background: linear-gradient(135deg, #ec4899, #f472b6); display: flex; align-items: center; justify-content: center;"><i class="fas fa-hashtag text-white text-xl"></i></div><div><div style="font-weight: 600; color: #ec4899;">#${escapeHtml(r.data.tag)}</div><div style="font-size: 12px; color: #8e8e8e;">${r.data.count} منشور</div></div></div>`;
    }
    document.getElementById('searchResults').innerHTML = html || '<div class="text-center p-4 text-gray-500">لا توجد نتائج</div>';
}

// ==================== الإشعارات ====================
async function loadNotifications() {
    if (!currentUser) return;
    db.ref(`notifications/${currentUser.uid}`).on('value', (snapshot) => {
        const ns = snapshot.val();
        const ni = document.querySelector('.nav-item:nth-child(4) i');
        if (!ni) return;
        const p = ni.parentElement;
        const eb = p.querySelector('.notification-badge');
        if (ns) {
            const ur = Object.values(ns).filter(n => !n.read).length;
            if (ur > 0) { if (!eb) p.innerHTML = '<i class="far fa-bell"></i><div class="notification-badge">' + ur + '</div>'; else eb.textContent = ur; }
            else if (eb) p.innerHTML = '<i class="far fa-bell"></i>';
        } else if (eb) p.innerHTML = '<i class="far fa-bell"></i>';
    });
}

async function openNotifications() {
    const s = await db.ref(`notifications/${currentUser.uid}`).once('value');
    const ns = s.val();
    const c = document.getElementById('notificationsList');
    if (!ns) { c.innerHTML = '<div class="text-center p-4 text-gray-500">لا توجد إشعارات</div>'; }
    else {
        c.innerHTML = Object.entries(ns).sort((a, b) => b[1].timestamp - a[1].timestamp).map(([id, n]) => `<div class="follower-item" onclick="markNotificationRead('${id}'); ${n.type === 'like' ? `openComments('${n.postId}')` : n.type === 'comment' ? `openComments('${n.postId}')` : `openProfile('${n.userId}')`}"><div class="post-avatar" style="width: 44px; height: 44px; background: linear-gradient(135deg, #ec4899, #f472b6); display: flex; align-items: center; justify-content: center;"><i class="fas ${n.type === 'like' ? 'fa-heart' : n.type === 'comment' ? 'fa-comment' : 'fa-user-plus'} text-white"></i></div><div style="flex: 1;"><div><span style="font-weight: 600;">${escapeHtml(n.userName)}</span> ${n.type === 'like' ? 'أعجب بمنشورك' : n.type === 'comment' ? `علق: ${n.text?.substring(0, 50)}` : 'بدأ بمتابعتك'}</div><div style="font-size: 11px; color: #8e8e8e;">${formatTime(n.timestamp)}</div></div></div>`).join('');
    }
    document.getElementById('notificationsPanel').classList.add('open');
    const up = {};
    for (const id of Object.keys(ns || {})) up[`notifications/${currentUser.uid}/${id}/read`] = true;
    await db.ref().update(up);
}

async function markNotificationRead(notifId) { await db.ref(`notifications/${currentUser.uid}/${notifId}`).update({ read: true }); }

// ==================== حفظ المنشورات ====================
async function savePost(postId) {
    const saveRef = db.ref(`savedPosts/${currentUser.uid}/${postId}`);
    const snapshot = await saveRef.once('value');
    if (snapshot.exists()) { await saveRef.remove(); showToast('تم إزالة من المحفوظة'); }
    else { await saveRef.set(true); showToast('تم حفظ المنشور 💖'); }
    refreshFeedCache();
}

async function openSavedPosts() {
    const snapshot = await db.ref(`savedPosts/${currentUser.uid}`).once('value');
    const savedPosts = snapshot.val();
    const container = document.getElementById('savedPostsGrid');
    if (!savedPosts) { container.innerHTML = '<div class="text-center p-8 text-gray-500" style="grid-column: span 3;">لا توجد منشورات محفوظة</div>'; }
    else {
        let html = '';
        for (const postId of Object.keys(savedPosts)) {
            const postSnapshot = await db.ref(`posts/${postId}`).once('value');
            const post = postSnapshot.val();
            if (post) {
                html += `<div class="grid-item" onclick="openComments('${postId}')">${post.mediaUrl ? (post.mediaType === 'image' ? `<img src="${post.mediaUrl}">` : `<video src="${post.mediaUrl}"></video>`) : '<div class="flex items-center justify-center h-full"><i class="fas fa-file-alt text-2xl text-gray-500"></i></div>'}</div>`;
            }
        }
        container.innerHTML = html || '<div class="text-center p-8 text-gray-500" style="grid-column: span 3;">لا توجد منشورات محفوظة</div>';
    }
    document.getElementById('savedPostsPanel').classList.add('open');
}

function closeSavedPosts() { document.getElementById('savedPostsPanel').classList.remove('open'); }

// ==================== الإبلاغ ====================
function openReportModal(postId) {
    currentReportPostId = postId;
    selectedReportReason = null;
    document.querySelectorAll('.report-reason').forEach(el => el.classList.remove('selected'));
    document.getElementById('reportModal').classList.add('open');
}

function selectReportReason(element, reason) {
    document.querySelectorAll('.report-reason').forEach(el => el.classList.remove('selected'));
    element.classList.add('selected');
    selectedReportReason = reason;
}

function closeReportModal() {
    document.getElementById('reportModal').classList.remove('open');
    currentReportPostId = null;
    selectedReportReason = null;
}

async function submitReport() {
    if (!selectedReportReason || !currentReportPostId) return showToast('الرجاء اختيار سبب الإبلاغ');
    await db.ref(`reports/${currentReportPostId}`).push({
        reporterId: currentUser.uid, reporterName: currentUser.displayName || currentUser.name,
        reason: selectedReportReason, timestamp: Date.now()
    });
    showToast('تم إرسال البلاغ، شكراً لك');
    closeReportModal();
}

console.log('💖 VIBE Extras Module Ready');
