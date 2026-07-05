// 💖 VIBE 2026 - Profile Module
// ==================== الملف الشخصي ====================

async function openMyProfile() { if (currentUser) openProfile(currentUser.uid); }

async function openProfile(userId) {
    currentProfileUser = userId;
    const snapshot = await db.ref(`users/${userId}`).once('value');
    const userData = snapshot.val();
    if (!userData) return;
    await recordProfileView(userId);
    const pc = document.getElementById('profileCover');
    if (pc) { pc.style.backgroundImage = userData.cover ? `url(${userData.cover})` : 'linear-gradient(135deg, #ec4899, #f472b6)'; pc.style.backgroundSize = 'cover'; pc.style.backgroundPosition = 'center'; }
    document.getElementById('profileAvatarLarge').innerHTML = userData.avatar ? `<img src="${userData.avatar}" style="width:100%;height:100%;object-fit:cover">` : '<i class="fas fa-user text-5xl text-white flex items-center justify-center h-full"></i>';
    
    // 💎 Verified Badge in Profile
    const verifiedBadgeHtml = userData.verified ? getVerifiedBadge('lg') : '';
    document.getElementById('profileName').innerHTML = `${escapeHtml(userData.name)} ${verifiedBadgeHtml}`;
    document.getElementById('profileBio').textContent = userData.bio || "مرحباً! أنا في VIBE ✨";
    const we = document.getElementById('profileWebsite');
    we.innerHTML = userData.website ? `<a href="${userData.website}" target="_blank" style="color: #ec4899;">${userData.website}</a>` : '';
    
    const fs = await db.ref(`followers/${userId}`).once('value');
    const fgs = await db.ref(`following/${userId}`).once('value');
    const vs = await db.ref(`profileViews/${userId}`).once('value');
    document.getElementById('profileFollowersCount').textContent = fs.exists() ? Object.keys(fs.val()).length : 0;
    document.getElementById('profileFollowingCount').textContent = fgs.exists() ? Object.keys(fgs.val()).length : 0;
    document.getElementById('profileViewsCount').textContent = vs.exists() ? Object.keys(vs.val()).length : 0;
    
    const ps = await db.ref('posts').once('value');
    const posts = ps.val();
    document.getElementById('profilePostsCount').textContent = posts ? Object.values(posts).filter(p => p.userId === userId).length : 0;
    
    const bd = document.getElementById('profileButtons');
    if (userId !== currentUser.uid) {
        const isF = await checkIfFollowing(userId);
        const isB = await isBlocked(userId);
        bd.innerHTML = `<button class="profile-btn ${isF ? '' : 'profile-btn-primary'}" onclick="toggleFollow('${userId}')">${isF ? 'متابَع' : 'متابعة'}</button><button class="profile-btn" onclick="openChat('${userId}')"><i class="fas fa-comment"></i> راسل</button><button class="profile-btn" onclick="startVideoCallWithUser('${userId}')"><i class="fas fa-video"></i></button>${isB ? `<button class="profile-btn" onclick="unblockUser('${userId}')">إلغاء الحظر</button>` : `<button class="profile-btn" onclick="blockUser('${userId}')">حظر</button>`}`;
    } else {
        let ab = (currentUser.isAdmin || currentUser.email === ADMIN_EMAIL) ? `<button class="profile-btn profile-btn-primary" onclick="openAdminPanel()"><i class="fas fa-cog"></i> لوحة التحكم</button>` : '';
        bd.innerHTML = `<button class="profile-btn" onclick="openEditProfileModal()"><i class="fas fa-edit"></i> تعديل</button><button class="profile-btn" onclick="changeAvatar()"><i class="fas fa-camera"></i> صورة</button><button class="profile-btn" onclick="changeCover()"><i class="fas fa-image"></i> غلاف</button>${ab}`;
    }
    await loadProfilePosts(userId);
    document.getElementById('profilePanel').classList.add('open');
}

async function checkIfFollowing(userId) { const s = await db.ref(`followers/${userId}/${currentUser.uid}`).once('value'); return s.exists(); }

async function toggleFollow(userId) {
    const isF = await checkIfFollowing(userId);
    if (isF) { await db.ref(`followers/${userId}/${currentUser.uid}`).remove(); await db.ref(`following/${currentUser.uid}/${userId}`).remove(); showToast('تم إلغاء المتابعة'); }
    else {
        await db.ref(`followers/${userId}/${currentUser.uid}`).set({ uid: currentUser.uid, name: currentUser.displayName || currentUser.name, timestamp: Date.now() });
        await db.ref(`following/${currentUser.uid}/${userId}`).set({ uid: userId, timestamp: Date.now() });
        showToast('تم المتابعة 💖');
        const ds = await db.ref(`users/${userId}/dnd`).once('value');
        if (!ds.val()) await db.ref(`notifications/${userId}`).push({ type: 'follow', userId: currentUser.uid, userName: currentUser.displayName || currentUser.name, timestamp: Date.now(), read: false });
    }
    openProfile(userId);
}

async function loadProfilePosts(userId) {
    const ps = await db.ref('posts').once('value');
    const posts = ps.val();
    const ups = posts ? Object.values(posts).filter(p => p.userId === userId).sort((a, b) => b.timestamp - a.timestamp) : [];
    const grid = document.getElementById('profilePostsGrid');
    if (!grid) return;
    if (!ups.length) { grid.innerHTML = '<div class="text-center p-8 text-gray-500" style="grid-column: span 3;">لا توجد منشورات</div>'; return; }
    grid.innerHTML = ups.map(p => `<div class="grid-item" onclick="openComments('${p.id}')">${p.mediaUrl ? (p.mediaType === 'image' ? `<img src="${p.mediaUrl}">` : `<video src="${p.mediaUrl}"></video>`) : '<div class="flex items-center justify-center h-full"><i class="fas fa-file-alt text-2xl text-gray-500"></i></div>'}<div class="grid-item-overlay"><span><i class="fas fa-heart"></i> ${p.likes ? Object.keys(p.likes).length : 0}</span><span><i class="fas fa-comment"></i> ${p.commentsCount || 0}</span></div></div>`).join('');
}

async function loadProfileMedia(userId) {
    const ps = await db.ref('posts').once('value');
    const posts = ps.val();
    const ups = posts ? Object.values(posts).filter(p => p.userId === userId && p.mediaUrl).sort((a, b) => b.timestamp - a.timestamp) : [];
    const grid = document.getElementById('profilePostsGrid');
    if (!grid) return;
    if (!ups.length) { grid.innerHTML = '<div class="text-center p-8 text-gray-500" style="grid-column: span 3;">لا توجد وسائط</div>'; return; }
    grid.innerHTML = ups.map(p => `<div class="grid-item" onclick="openComments('${p.id}')">${p.mediaType === 'image' ? `<img src="${p.mediaUrl}">` : `<video src="${p.mediaUrl}"></video>`}</div>`).join('');
}

function openEditProfileModal() {
    document.getElementById('editName').value = currentUser.displayName || currentUser.name || '';
    document.getElementById('editBio').value = currentUser.bio || '';
    document.getElementById('editWebsite').value = currentUser.website || '';
    document.getElementById('editProfileModal').classList.add('open');
}
function closeEditProfileModal() { document.getElementById('editProfileModal').classList.remove('open'); }

async function saveProfileEdit() {
    const nn = document.getElementById('editName')?.value;
    const nb = document.getElementById('editBio')?.value;
    const nw = document.getElementById('editWebsite')?.value;
    if (nn && nn.trim()) await currentUser.updateProfile({ displayName: nn.trim() });
    await db.ref(`users/${currentUser.uid}`).update({ name: nn || currentUser.name, bio: nb || "", website: nw || "" });
    currentUser.name = nn || currentUser.name; currentUser.bio = nb || ""; currentUser.website = nw || "";
    currentUser.displayName = nn || currentUser.displayName;
    closeEditProfileModal(); openProfile(currentUser.uid); showToast('تم حفظ التغييرات 💖');
}

// ==================== مشاهدات الملف الشخصي ====================
async function recordProfileView(viewedUserId) {
    if (viewedUserId === currentUser.uid) return;
    await db.ref(`profileViews/${viewedUserId}/${currentUser.uid}`).set({
        viewerId: currentUser.uid, viewerName: currentUser.displayName || currentUser.name,
        viewerAvatar: currentUser.avatar || '', timestamp: Date.now()
    });
}

async function openProfileViews() {
    const snapshot = await db.ref(`profileViews/${currentProfileUser || currentUser.uid}`).once('value');
    const views = snapshot.val();
    const container = document.getElementById('profileViewsList');
    if (!views) {
        container.innerHTML = '<div class="text-center p-4 text-gray-500">لا توجد مشاهدات بعد</div>';
    } else {
        let html = '';
        const viewsArray = Object.values(views).sort((a, b) => b.timestamp - a.timestamp).slice(0, 50);
        for (const view of viewsArray) {
            // 💎 Check if viewer is verified
            const viewerSnap = await db.ref(`users/${view.viewerId}`).once('value');
            const viewerData = viewerSnap.val();
            const vBadge = viewerData?.verified ? getVerifiedBadge('sm') : '';
            html += `<div class="follower-item" onclick="closeProfileViews(); openProfile('${view.viewerId}')">
                <div class="post-avatar" style="width: 44px; height: 44px;">${view.viewerAvatar ? `<img src="${view.viewerAvatar}">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>'}</div>
                <div><div style="font-weight: 600;">${vBadge}${escapeHtml(view.viewerName)}</div><div style="font-size: 11px; color: #8e8e8e;">${formatTime(view.timestamp)}</div></div>
            </div>`;
        }
        container.innerHTML = html;
    }
    document.getElementById('profileViewsPanel').classList.add('open');
}

function closeProfileViews() { document.getElementById('profileViewsPanel').classList.remove('open'); }

// ==================== المتابعون ====================
async function openFollowersList(type) {
    document.getElementById('followersTitle').textContent = type === 'followers' ? 'المتابعون' : 'المتابَعون';
    const rp = type === 'followers' ? `followers/${currentProfileUser}` : `following/${currentProfileUser}`;
    const s = await db.ref(rp).once('value');
    const data = s.val();
    const c = document.getElementById('followersList');
    if (!data) { c.innerHTML = '<div class="text-center p-4 text-gray-500">لا يوجد</div>'; }
    else {
        let html = '';
        for (const [uid] of Object.entries(data)) {
            const us = await db.ref(`users/${uid}`).once('value');
            const ud = us.val();
            const vBadge = ud?.verified ? getVerifiedBadge('sm') : '';
            html += `<div class="follower-item" onclick="closeFollowers(); openProfile('${uid}')"><div class="post-avatar" style="width: 48px; height: 48px;">${ud?.avatar ? `<img src="${ud.avatar}">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>'}</div><div><div style="font-weight: 600;">${vBadge}${escapeHtml(ud?.name || 'مستخدم')}</div></div></div>`;
        }
        c.innerHTML = html;
    }
    document.getElementById('followersPanel').classList.add('open');
}
function closeFollowers() { document.getElementById('followersPanel').classList.remove('open'); }

console.log('💖 VIBE Profile Module Ready');
