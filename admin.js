// 💖 VIBE 2026 - Admin Panel Module

// ==================== الكلمات الممنوعة ====================
async function loadBadWordsList() {
    const snapshot = await db.ref('badWords').once('value');
    const words = snapshot.val();
    badWordsList = words ? Object.values(words) : [];
    console.log('📝 الكلمات الممنوعة:', badWordsList);
}

async function addBadWord(word) {
    if (!word.trim()) return;
    await db.ref('badWords').push(word.trim().toLowerCase());
    await loadBadWordsList();
    showToast(`تمت إضافة كلمة: ${word}`);
    if (currentUser?.isAdmin) openAdminPanel();
}

async function removeBadWord(wordId, word) {
    await db.ref(`badWords/${wordId}`).remove();
    await loadBadWordsList();
    showToast(`تم حذف كلمة: ${word}`);
    if (currentUser?.isAdmin) openAdminPanel();
}

function showAddBadWordModal() {
    const word = prompt('📝 أدخل الكلمة التي تريد منعها:');
    if (word && word.trim()) addBadWord(word.trim());
}

// ==================== حظر وتقييد ====================
async function muteUser(userId, minutes = 60) {
    const muteUntil = Date.now() + (minutes * 60 * 1000);
    await db.ref(`users/${userId}/mutedUntil`).set(muteUntil);
    showToast(`تم تقييد المستخدم لمدة ${minutes} دقيقة`);
    openAdminPanel();
}

async function isUserMuted(userId) {
    const snapshot = await db.ref(`users/${userId}/mutedUntil`).once('value');
    const muteUntil = snapshot.val();
    return muteUntil && muteUntil > Date.now();
}

async function blockUser(userId) { await db.ref(`users/${currentUser.uid}/blockedUsers/${userId}`).set(true); showToast('تم حظر المستخدم'); refreshFeedCache(); }
async function unblockUser(userId) { await db.ref(`users/${currentUser.uid}/blockedUsers/${userId}`).remove(); showToast('تم إلغاء حظر المستخدم'); refreshFeedCache(); }
async function isBlocked(userId) { const snapshot = await db.ref(`users/${currentUser.uid}/blockedUsers/${userId}`).once('value'); return snapshot.exists(); }

// ==================== لوحة التحكم ====================
async function openAdminPanel() {
    if (currentUser.email !== ADMIN_EMAIL && !currentUser.isAdmin) return showToast('🚫 غير مصرح لك بالدخول إلى لوحة التحكم');
    showToast('💖 جاري تحميل لوحة التحكم...');
    
    // Bad Words
    const bws = await db.ref('badWords').once('value');
    const bw = bws.val();
    const bwc = document.getElementById('badWordsList');
    if (bwc) {
        if (!bw) bwc.innerHTML = '<div class="text-center p-4 text-gray-500">لا توجد كلمات ممنوعة</div>';
        else bwc.innerHTML = Object.entries(bw).map(([id, w]) => `<div class="admin-item"><div><span style="font-weight: 600;">🚫 ${escapeHtml(w)}</span></div><button onclick="removeBadWord('${id}', '${w}')" style="background: #ef4444; color: white; border: none; padding: 6px 12px; border-radius: 8px; cursor: pointer;">حذف</button></div>`).join('');
    }
    
    // Stats
    const uss = await db.ref('users').once('value');
    const pss = await db.ref('posts').once('value');
    const css = await db.ref('comments').once('value');
    document.getElementById('adminUsersCount').textContent = uss.exists() ? Object.keys(uss.val()).length : 0;
    document.getElementById('adminPostsCount').textContent = pss.exists() ? Object.keys(pss.val()).length : 0;
    let cc = 0;
    if (css.exists()) for (const pc of Object.values(css.val())) cc += Object.keys(pc).length;
    document.getElementById('adminCommentsCount').textContent = cc;
    
    // Users Management with Verify Toggle
    let usersHtml = '';
    if (uss.exists()) {
        for (const [uid, user] of Object.entries(uss.val())) {
            if (uid !== currentUser.uid) {
                const isMuted = await isUserMuted(uid);
                const isUserVerified = user.verified || false;
                // 💎 Verified Badge in Admin + Verify Button
                const verifyBtn = isUserVerified 
                    ? `<button class="admin-verify-btn unverify" onclick="toggleVerifyUser('${uid}')"><i class="fas fa-times-circle"></i> إلغاء التوثيق</button>`
                    : `<button class="admin-verify-btn" onclick="toggleVerifyUser('${uid}')"><i class="fas fa-check-circle"></i> توثيق</button>`;
                const vBadge = isUserVerified ? getVerifiedBadge('sm') : '';
                usersHtml += `<div class="admin-item">
                    <div>
                        <div class="admin-item-name">${vBadge}${escapeHtml(user.name)}</div>
                        <div style="font-size: 11px; color: #8e8e8e;">${escapeHtml(user.email)}</div>
                    </div>
                    <div>
                        ${verifyBtn}
                        <button onclick="muteUser('${uid}', 60)" style="background: #f59e0b; color: white; border: none; padding: 6px 12px; border-radius: 8px; cursor: pointer; font-size: 12px; margin: 0 4px;">🔇 تقييد</button>
                        <button onclick="deleteUser('${uid}')" style="background: #ef4444; color: white; border: none; padding: 6px 12px; border-radius: 8px; cursor: pointer; font-size: 12px;">🗑️ حذف</button>
                    </div>
                </div>`;
            }
        }
    }
    document.getElementById('adminUsersList').innerHTML = usersHtml || '<div class="text-center p-4 text-gray-500">لا يوجد مستخدمين</div>';
    
    // Posts Management
    let postsHtml = '';
    if (pss.exists()) {
        for (const post of Object.values(pss.val()).sort((a, b) => b.timestamp - a.timestamp).slice(0, 20)) {
            postsHtml += `<div class="admin-item"><div><div style="font-weight: 600;">${escapeHtml(post.userName)}</div><div style="font-size: 11px; color: #8e8e8e;">${escapeHtml(post.text?.substring(0, 50) || '')}</div></div><button onclick="deletePost('${post.id}')" style="background: #ef4444; color: white; border: none; padding: 6px 12px; border-radius: 8px; cursor: pointer;">🗑️ حذف</button></div>`;
        }
    }
    document.getElementById('adminPostsList').innerHTML = postsHtml || '<div class="text-center p-4 text-gray-500">لا توجد منشورات</div>';
    
    document.getElementById('adminPanel').classList.add('open');
}

// 💎 Toggle Verify User
async function toggleVerifyUser(userId) {
    const snap = await db.ref(`users/${userId}`).once('value');
    const data = snap.val();
    if (!data) return;
    const newState = !data.verified;
    if (!confirm(`تأكيد ${newState ? 'توثيق' : 'إلغاء توثيق'} @${data.name || 'المستخدم'}؟`)) return;
    await db.ref(`users/${userId}`).update({ 
        verified: newState, 
        verifiedAt: newState ? Date.now() : null, 
        verifiedBy: newState ? currentUser.uid : null 
    });
    showToast(`✅ تم ${newState ? 'توثيق' : 'إلغاء توثيق'} المستخدم`);
    openAdminPanel();
    if (currentProfileUser === userId) openProfile(userId);
    refreshFeedCache();
}

async function deleteUser(userId) {
    if (confirm('⚠️ هل أنت متأكد من حذف هذا المستخدم نهائياً؟')) {
        await db.ref(`users/${userId}`).remove();
        showToast('🗑️ تم حذف المستخدم');
        openAdminPanel();
        refreshFeedCache();
    }
}

function closeAdmin() { document.getElementById('adminPanel').classList.remove('open'); }

console.log('💖 VIBE Admin Module Ready');
