// 💖 VIBE 2026 - Posts & Comments Module

// ==================== إنشاء منشور ====================
function createHeartAnimation(x, y) {
    const heart = document.createElement('div');
    heart.className = 'heart-animation';
    heart.innerHTML = '❤️';
    heart.style.left = x + 'px';
    heart.style.top = y + 'px';
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 600);
}

function addEmojiToPost(emoji) {
    const textarea = document.getElementById('postText');
    textarea.value += emoji;
    textarea.focus();
}

function openStickerPicker() {
    const picker = document.getElementById('stickerPicker');
    picker.style.display = picker.style.display === 'grid' ? 'none' : 'grid';
}

function addPollToCompose() {
    const pollBuilder = document.getElementById('pollBuilder');
    pollBuilder.style.display = pollBuilder.style.display === 'none' ? 'block' : 'none';
    if (pollBuilder.style.display === 'none') {
        document.getElementById('pollQuestion').value = '';
        document.getElementById('pollOption1').value = '';
        document.getElementById('pollOption2').value = '';
    }
}

function addPollOption() {
    const container = document.getElementById('pollBuilder');
    const inputCount = container.querySelectorAll('input[type="text"]').length;
    if (inputCount < 6) {
        const newInput = document.createElement('input');
        newInput.type = 'text';
        newInput.placeholder = `خيار ${inputCount + 1}`;
        newInput.className = 'chat-input';
        newInput.style.width = '100%';
        newInput.style.marginBottom = '4px';
        container.insertBefore(newInput, container.querySelector('button'));
    } else { showToast('لا يمكن إضافة أكثر من 6 خيارات'); }
}

function toggleSchedulePicker() {
    const picker = document.getElementById('schedulePicker');
    picker.style.display = picker.style.display === 'none' ? 'block' : 'none';
}

async function schedulePost() {
    const scheduleDate = document.getElementById('scheduleDate').value;
    if (!scheduleDate) return showToast('الرجاء تحديد تاريخ ووقت');
    const scheduleTime = new Date(scheduleDate).getTime();
    if (scheduleTime <= Date.now()) return showToast('الرجاء تحديد وقت مستقبلي');
    const text = document.getElementById('postText').value;
    if (!text && !selectedMediaFile) return showToast('الرجاء كتابة نص أو إضافة وسائط');
    
    const scheduledPost = {
        userId: currentUser.uid, userName: currentUser.displayName || currentUser.name,
        userAvatar: currentUser.avatar || "", text: text,
        mediaUrl: selectedMediaFile ? await uploadToCloudinary(selectedMediaFile) : "",
        mediaType: selectedMediaFile ? selectedMediaFile.type.split('/')[0] : "",
        scheduleTime: scheduleTime, timestamp: Date.now()
    };
    await db.ref(`scheduledPosts/${currentUser.uid}`).push(scheduledPost);
    showToast('تم جدولة المنشور');
    closeCompose();
    checkScheduledPosts();
}

async function checkScheduledPosts() {
    const snapshot = await db.ref(`scheduledPosts/${currentUser.uid}`).once('value');
    const scheduled = snapshot.val();
    if (scheduled) {
        for (const [id, post] of Object.entries(scheduled)) {
            if (post.scheduleTime <= Date.now()) {
                const postRef = db.ref('posts').push();
                await postRef.set({
                    id: postRef.key, userId: post.userId, userName: post.userName,
                    userAvatar: post.userAvatar, text: post.text, mediaUrl: post.mediaUrl,
                    mediaType: post.mediaType, hashtags: extractHashtags(post.text),
                    likes: {}, views: 0, commentsCount: 0, edited: false, timestamp: Date.now()
                });
                await db.ref(`scheduledPosts/${currentUser.uid}/${id}`).remove();
                showToast('تم نشر المنشور المجدول');
                await refreshFeedCache();
            }
        }
    }
}

async function createPost() {
    const publishBtn = document.getElementById('publishPostBtn');
    if (publishBtn) { publishBtn.style.transform = 'scale(0.95)'; setTimeout(() => { if(publishBtn) publishBtn.style.transform = 'scale(1)'; }, 150); }
    
    let text = document.getElementById('postText')?.value;
    if (containsBadWords(text)) return showToast('⚠️ المنشور يحتوي على كلمات ممنوعة');
    if (!text && !selectedMediaFile) return showToast('الرجاء كتابة نص أو إضافة وسائط');
    text = filterBadWords(text);
    if (await isUserMuted(currentUser.uid)) return showToast('⚠️ أنت مقيد مؤقتاً ولا يمكنك النشر');

    let mediaUrl = "", mediaType = "";
    if (selectedMediaFile) {
        mediaType = selectedMediaFile.type.split('/')[0];
        mediaUrl = await uploadToCloudinary(selectedMediaFile);
        if (!mediaUrl) return;
    }

    const hashtags = extractHashtags(text);
    const postRef = db.ref('posts').push();
    
    let quoteData = null;
    if (window.quoteOriginalPostId) {
        const originalPostSnapshot = await db.ref(`posts/${window.quoteOriginalPostId}`).once('value');
        const originalPost = originalPostSnapshot.val();
        if (originalPost) { quoteData = { originalPostId: window.quoteOriginalPostId, originalText: originalPost.text, originalUser: originalPost.userName }; }
        delete window.quoteOriginalPostId;
    }
    
    let pollData = null;
    const pollQuestion = document.getElementById('pollQuestion')?.value;
    if (pollQuestion) {
        const options = [];
        const optionInputs = document.querySelectorAll('#pollBuilder input[type="text"]');
        for (let i = 0; i < optionInputs.length; i++) { if (optionInputs[i].value) options.push(optionInputs[i].value); }
        if (options.length >= 2) { pollData = { question: pollQuestion, options: options, votes: {}, totalVotes: 0 }; }
    }
    
    await postRef.set({
        id: postRef.key, userId: currentUser.uid, userName: currentUser.displayName || currentUser.name,
        userAvatar: currentUser.avatar || "", text: text, mediaUrl: mediaUrl, mediaType: mediaType,
        hashtags: hashtags, likes: {}, views: 0, commentsCount: 0, edited: false,
        quote: quoteData, poll: pollData, timestamp: Date.now()
    });
    
    for (const tag of hashtags) { await db.ref(`hashtags/${tag.toLowerCase()}/${postRef.key}`).set(true); }

    document.getElementById('postText').value = "";
    document.getElementById('mediaPreview').innerHTML = "";
    document.getElementById('mediaPreview').style.display = "none";
    document.getElementById('pollBuilder').style.display = "none";
    selectedMediaFile = null;
    closeCompose();
    await refreshFeedCache();
    loadTrendingHashtags();
    showToast('تم نشر المنشور بنجاح 💖');
}

// ==================== حذف منشور ====================
async function deletePost(postId) {
    if (!confirm('هل أنت متأكد من حذف هذا المنشور؟')) return;
    const postSnapshot = await db.ref(`posts/${postId}`).once('value');
    const post = postSnapshot.val();
    if (post.userId !== currentUser.uid && !currentUser.isAdmin) return showToast('لا يمكنك حذف منشور ليس لك');
    if (post.hashtags) { for (const tag of post.hashtags) { await db.ref(`hashtags/${tag.toLowerCase()}/${postId}`).remove(); } }
    await db.ref(`posts/${postId}`).remove();
    await refreshFeedCache();
    loadTrendingHashtags();
    showToast('تم حذف المنشور');
}

// ==================== إعجاب ====================
async function likePost(postId) {
    const likeRef = db.ref(`posts/${postId}/likes/${currentUser.uid}`);
    const snapshot = await likeRef.once('value');
    const wasLiked = snapshot.exists();
    
    const postCard = document.querySelector(`.post-card[data-post-id="${postId}"]`);
    if (postCard) {
        const likeButton = postCard.querySelector('.post-action:first-child');
        const likesSpan = postCard.querySelector('.post-likes');
        if (likeButton) { wasLiked ? likeButton.classList.remove('active') : likeButton.classList.add('active'); }
        if (likesSpan && !hideLikesActive) {
            let currentCount = parseInt(likesSpan.textContent) || 0;
            currentCount = wasLiked ? currentCount - 1 : currentCount + 1;
            likesSpan.textContent = `${currentCount} إعجاب`;
            likesSpan.style.display = currentCount === 0 ? 'none' : 'block';
        }
    }
    
    if (wasLiked) { await likeRef.remove(); }
    else {
        await likeRef.set(true);
        const postSnapshot = await db.ref(`posts/${postId}`).once('value');
        const post = postSnapshot.val();
        if (post && post.userId !== currentUser.uid) {
            const dndSnapshot = await db.ref(`users/${post.userId}/dnd`).once('value');
            if (!dndSnapshot.val()) {
                await db.ref(`notifications/${post.userId}`).push({
                    type: 'like', userId: currentUser.uid, userName: currentUser.displayName || currentUser.name,
                    postId: postId, timestamp: Date.now(), read: false
                });
            }
        }
    }
}

// ==================== مشاركة وتصويت ====================
async function sharePost(postId) {
    const postSnapshot = await db.ref(`posts/${postId}`).once('value');
    const post = postSnapshot.val();
    const shareRef = db.ref('posts').push();
    await shareRef.set({
        id: shareRef.key, userId: currentUser.uid, userName: currentUser.displayName || currentUser.name,
        userAvatar: currentUser.avatar || "", text: `شارك منشور: ${post.text.substring(0, 100)}`,
        originalPostId: postId, originalUser: post.userName, timestamp: Date.now()
    });
    await refreshFeedCache();
    showToast('تمت المشاركة 💖');
}

async function votePoll(postId, optionIndex) {
    const postRef = db.ref(`posts/${postId}/poll`);
    const snapshot = await postRef.once('value');
    const poll = snapshot.val();
    if (poll && poll.votes && poll.votes[currentUser.uid]) return showToast('لقد صوت مسبقاً');
    await db.ref(`posts/${postId}/poll/votes/${currentUser.uid}`).set(optionIndex);
    await db.ref(`posts/${postId}/poll/totalVotes`).transaction(current => (current || 0) + 1);
    refreshFeedCache();
}

async function incrementPostViews(postId) {
    await db.ref(`posts/${postId}/views`).transaction(current => (current || 0) + 1);
}

// ==================== تثبيت واقتباس ====================
async function pinComment(postId, commentId) {
    await db.ref(`posts/${postId}/pinnedComment`).set(commentId);
    showToast('تم تثبيت التعليق');
    loadComments(postId);
}

function quotePost(postId, originalText, originalUser) {
    openCompose();
    document.getElementById('postText').value = `اقتباس من @${originalUser}: "${originalText.substring(0, 100)}"\n\n`;
    window.quoteOriginalPostId = postId;
}

async function pinPost(postId) {
    const currentPinned = await db.ref(`users/${currentUser.uid}/pinnedPost`).once('value');
    if (currentPinned.val() === postId) {
        await db.ref(`users/${currentUser.uid}/pinnedPost`).remove();
        showToast('تم إلغاء تثبيت المنشور');
    } else {
        await db.ref(`users/${currentUser.uid}/pinnedPost`).set(postId);
        showToast('تم تثبيت المنشور 📌');
    }
    refreshFeedCache();
}

// ==================== التعليقات ====================
async function openComments(postId) { currentPostId = postId; document.getElementById('commentsPanel').classList.add('open'); await loadComments(postId); }

async function loadComments(postId) {
    const snapshot = await db.ref(`comments/${postId}`).once('value');
    const comments = snapshot.val();
    const commentsList = document.getElementById('commentsList');
    if (!commentsList) return;
    const pinnedCommentId = await db.ref(`posts/${postId}/pinnedComment`).once('value');
    const pinnedId = pinnedCommentId.val();
    if (!comments) { commentsList.innerHTML = '<div class="text-center p-4 text-gray-500">لا توجد تعليقات</div>'; return; }
    let commentsArray = Object.entries(comments).map(([id, comment]) => ({ id, ...comment }));
    if (pinnedId) { const pi = commentsArray.findIndex(c => c.id === pinnedId); if (pi > -1) { const pc = commentsArray[pi]; commentsArray.splice(pi, 1); commentsArray.unshift(pc); } }
    let html = '';
    for (const comment of commentsArray) {
        const userSnapshot = await db.ref(`users/${comment.userId}`).once('value');
        const userData = userSnapshot.val();
        // 💎 Verified Badge in Comments
        const vBadge = userData?.verified ? getVerifiedBadge('sm') : '';
        html += `<div class="chat-message"><div class="message-bubble"><div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;"><span style="font-weight: 600; cursor: pointer;" onclick="closeComments(); openProfile('${comment.userId}')">${vBadge}${escapeHtml(userData?.name || 'مستخدم')}</span><span style="font-size: 10px; color: #8e8e8e;">${formatTime(comment.timestamp)}</span>${comment.id === pinnedId ? '<span style="background: #ec4899; color: white; padding: 2px 6px; border-radius: 12px; font-size: 9px;">📌 مثبت</span>' : ''}</div><div>${escapeHtml(filterBadWords(comment.text))}</div></div></div>`;
    }
    commentsList.innerHTML = html;
}

async function addComment() {
    let text = document.getElementById('commentInput')?.value;
    if (!text || !currentPostId) return;
    if (containsBadWords(text)) return showToast('⚠️ التعليق يحتوي على كلمات ممنوعة');
    text = filterBadWords(text);
    if (await isUserMuted(currentUser.uid)) return showToast('⚠️ أنت مقيد مؤقتاً');
    const commentRef = db.ref(`comments/${currentPostId}`).push();
    await commentRef.set({ userId: currentUser.uid, userName: currentUser.displayName || currentUser.name, text, timestamp: Date.now() });
    const postRef = db.ref(`posts/${currentPostId}`);
    const snapshot = await postRef.once('value');
    const post = snapshot.val();
    await postRef.update({ commentsCount: (post.commentsCount || 0) + 1 });
    if (post.userId !== currentUser.uid) {
        const dndSnapshot = await db.ref(`users/${post.userId}/dnd`).once('value');
        if (!dndSnapshot.val()) {
            await db.ref(`notifications/${post.userId}`).push({ type: 'comment', userId: currentUser.uid, userName: currentUser.displayName || currentUser.name, postId: currentPostId, text, timestamp: Date.now(), read: false });
        }
    }
    document.getElementById('commentInput').value = '';
    await loadComments(currentPostId);
    refreshFeedCache();
    showToast('تم إضافة التعليق 💬');
}

// ==================== Infinite Scroll ====================
async function loadAllPostsToCache() {
    const feedContainer = document.getElementById('feedContainer');
    if (!feedContainer) return;
    feedContainer.innerHTML = '<div class="loading"><div class="spinner"></div><span>جاري التحميل...</span></div>';
    
    const snapshot = await db.ref('posts').once('value');
    const posts = snapshot.val();
    if (!posts || Object.keys(posts).length === 0) {
        feedContainer.innerHTML = '<div class="text-center p-8 text-gray-500">💖 لا توجد منشورات بعد</div>';
        hasMorePosts = false; return;
    }
    
    let postsArray = Object.values(posts).sort((a, b) => b.timestamp - a.timestamp);
    if (currentUser) {
        const blockedSnapshot = await db.ref(`users/${currentUser.uid}/blockedUsers`).once('value');
        const blockedUsers = blockedSnapshot.val() || {};
        postsArray = postsArray.filter(post => !blockedUsers[post.userId]);
        const pinnedPostId = await db.ref(`users/${currentUser.uid}/pinnedPost`).once('value');
        const pinnedId = pinnedPostId.val();
        if (pinnedId) {
            const pinnedIndex = postsArray.findIndex(p => p.id === pinnedId);
            if (pinnedIndex > -1) { const pp = postsArray[pinnedIndex]; postsArray.splice(pinnedIndex, 1); postsArray.unshift(pp); }
        }
    }
    
    allPostsCache = postsArray;
    hasMorePosts = allPostsCache.length > POSTS_PER_PAGE;
    currentDisplayCount = POSTS_PER_PAGE;
    feedContainer.innerHTML = '';
    await displayPosts(0, POSTS_PER_PAGE);
    if (!scrollListenerAdded) { setupScrollListener(); scrollListenerAdded = true; }
}

async function displayPosts(startIndex, count) {
    const feedContainer = document.getElementById('feedContainer');
    if (!feedContainer) return;
    const endIndex = Math.min(startIndex + count, allPostsCache.length);
    const postsToShow = allPostsCache.slice(startIndex, endIndex);
    
    for (const post of postsToShow) {
        await incrementPostViews(post.id);
        const userInfoSnapshot = await db.ref(`users/${post.userId}`).once('value');
        const userInfo = userInfoSnapshot.val();
        const isUserVerified = userInfo?.verified || false;
        const isLiked = post.likes && post.likes[currentUser?.uid];
        const likesCount = post.likes ? Object.keys(post.likes).length : 0;
        const isOwner = post.userId === currentUser?.uid;
        let isPinned = false;
        if (currentUser) { const pp = await db.ref(`users/${currentUser.uid}/pinnedPost`).once('value'); isPinned = pp.val() === post.id; }
        const savedSnapshot = currentUser ? await db.ref(`savedPosts/${currentUser.uid}/${post.id}`).once('value') : { exists: () => false };
        const isSaved = savedSnapshot.exists();
        
        let formattedText = escapeHtml(post.text);
        if (post.hashtags) post.hashtags.forEach(tag => { const regex = new RegExp(`#${tag}`, 'gi'); formattedText = formattedText.replace(regex, `<span class="post-hashtags" onclick="searchHashtag('${tag}')">#${tag}</span>`); });
        formattedText = formattedText.replace(/@(\w+)/g, '<span class="post-hashtags" onclick="searchUser(\'$1\')">@$1</span>');
        
        // 💎 Verified Badge in Posts
        const vBadgeHtml = isUserVerified ? getVerifiedBadge('main') : '';
        
        let pollHtml = '';
        if (post.poll && post.poll.question) {
            pollHtml = '<div class="poll-container"><div style="font-weight: 600; margin-bottom: 8px;">📊 ' + escapeHtml(post.poll.question) + '</div>';
            for (let i = 0; i < post.poll.options.length; i++) {
                const voteCount = post.poll.votes ? Object.values(post.poll.votes).filter(v => v === i).length : 0;
                const percentage = post.poll.totalVotes > 0 ? (voteCount / post.poll.totalVotes * 100).toFixed(1) : 0;
                pollHtml += `<div class="poll-option" onclick="votePoll('${post.id}', ${i})"><div class="poll-progress" style="width: ${percentage}%;"></div><div class="poll-option-text"><span>${escapeHtml(post.poll.options[i])}</span>${!hideLikesActive ? `<span>${percentage}% (${voteCount})</span>` : ''}</div></div>`;
            }
            pollHtml += `<div style="font-size: 11px; color: #8e8e8e; margin-top: 8px;">${post.poll.totalVotes || 0} صوت</div></div>`;
        }
        
        let quoteHtml = '';
        if (post.quote) {
            quoteHtml = `<div class="quote-post" onclick="openComments('${post.quote.originalPostId}')"><div style="font-weight: 600;">@${escapeHtml(post.quote.originalUser)}</div><div style="font-size: 13px;">${escapeHtml(post.quote.originalText?.substring(0, 100))}</div></div>`;
        }
        
        let mediaHtml = '';
        if (post.mediaUrl) {
            if (post.mediaType === 'image') mediaHtml = `<img src="${post.mediaUrl}" class="post-image" loading="lazy" onclick="event.stopPropagation(); openImageViewer(['${post.mediaUrl}'], 0)">`;
            else if (post.mediaType === 'video') {
                mediaHtml = `<div class="video-container" onclick="event.stopPropagation()"><video src="${post.mediaUrl}" class="post-video" autoplay muted loop playsinline></video><div class="video-controls"><button onclick="this.parentElement.parentElement.querySelector('video').play()"><i class="fas fa-play"></i></button><button onclick="this.parentElement.parentElement.querySelector('video').pause()"><i class="fas fa-pause"></i></button><button onclick="this.parentElement.parentElement.querySelector('video').muted = !this.parentElement.parentElement.querySelector('video').muted"><i class="fas fa-volume-up"></i></button></div></div>`;
            }
        }
        
        const postHtml = `
            <div class="post-card ${isPinned ? 'pinned' : ''} fade-in" data-post-id="${post.id}" ondblclick="likePost('${post.id}'); createHeartAnimation(event.clientX, event.clientY)">
                ${isPinned ? '<div class="pinned-badge"><i class="fas fa-thumbtack"></i> مثبت</div>' : ''}
                <div class="post-header">
                    <div class="post-user-info" onclick="openProfile('${post.userId}')">
                        <div class="post-avatar">${post.userAvatar ? `<img src="${post.userAvatar}">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>'}</div>
                        <div><div class="post-username">${escapeHtml(post.userName)}${vBadgeHtml}</div><div class="post-time">${formatTime(post.timestamp)} ${post.edited ? '· معدل' : ''}</div></div>
                    </div>
                    <div style="display: flex; gap: 12px;">
                        ${(isOwner || currentUser?.isAdmin) ? `<button class="post-menu" onclick="event.stopPropagation(); deletePost('${post.id}')"><i class="fas fa-trash-alt"></i></button>` : ''}
                        ${isOwner ? `<button class="post-menu" onclick="event.stopPropagation(); pinPost('${post.id}')"><i class="fas fa-thumbtack"></i></button>` : ''}
                        <button class="post-menu" onclick="event.stopPropagation(); savePost('${post.id}')"><i class="fas fa-bookmark" style="${isSaved ? 'color: #ec4899;' : ''}"></i></button>
                        <button class="post-menu" onclick="event.stopPropagation(); quotePost('${post.id}', '${escapeHtml(post.text)}', '${escapeHtml(post.userName)}')"><i class="fas fa-quote-right"></i></button>
                        <button class="post-menu" onclick="event.stopPropagation(); openReportModal('${post.id}')"><i class="fas fa-flag"></i></button>
                    </div>
                </div>
                ${mediaHtml}${pollHtml}${quoteHtml}
                <div class="post-actions">
                    <button class="post-action ${isLiked ? 'active' : ''}" onclick="likePost('${post.id}')"><i class="fas fa-heart"></i></button>
                    <button class="post-action" onclick="openComments('${post.id}')"><i class="fas fa-comment"></i></button>
                    <button class="post-action" onclick="sharePost('${post.id}')"><i class="fas fa-paper-plane"></i></button>
                </div>
                ${likesCount > 0 && !hideLikesActive ? `<div class="post-likes">${likesCount} إعجاب</div>` : ''}
                <div class="post-caption"><span onclick="openProfile('${post.userId}')">${escapeHtml(post.userName)}</span> ${formattedText}</div>
                ${post.commentsCount > 0 ? `<div class="post-comments" onclick="openComments('${post.id}')">عرض جميع التعليقات (${post.commentsCount})</div>` : ''}
                <div class="post-views"><i class="far fa-eye"></i> ${post.views || 0} مشاهدة</div>
            </div>`;
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
    } else { hasMorePosts = false; }
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
    window.addEventListener('scroll', handleScroll);
}

async function refreshFeedCache() {
    if (!currentUser) return;
    const snapshot = await db.ref('posts').once('value');
    const posts = snapshot.val();
    if (!posts || Object.keys(posts).length === 0) {
        allPostsCache = []; hasMorePosts = false; currentDisplayCount = 0;
        const fc = document.getElementById('feedContainer');
        if (fc) fc.innerHTML = '<div class="text-center p-8 text-gray-500">💖 لا توجد منشورات بعد</div>';
        return;
    }
    let postsArray = Object.values(posts).sort((a, b) => b.timestamp - a.timestamp);
    const blockedSnapshot = await db.ref(`users/${currentUser.uid}/blockedUsers`).once('value');
    const blockedUsers = blockedSnapshot.val() || {};
    postsArray = postsArray.filter(post => !blockedUsers[post.userId]);
    const pinnedPostId = await db.ref(`users/${currentUser.uid}/pinnedPost`).once('value');
    const pinnedId = pinnedPostId.val();
    if (pinnedId) { const pi = postsArray.findIndex(p => p.id === pinnedId); if (pi > -1) { const pp = postsArray[pi]; postsArray.splice(pi, 1); postsArray.unshift(pp); } }
    allPostsCache = postsArray;
    hasMorePosts = allPostsCache.length > POSTS_PER_PAGE;
    currentDisplayCount = Math.min(POSTS_PER_PAGE, allPostsCache.length);
    const fc = document.getElementById('feedContainer');
    if (fc) { fc.innerHTML = ''; await displayPosts(0, currentDisplayCount); }
}

function resetInfiniteScroll() { isLoadingPosts = false; hasMorePosts = true; allPostsCache = []; currentDisplayCount = 0; }
async function loadFeed() { await loadAllPostsToCache(); }

console.log('💖 VIBE Posts Module Ready');
