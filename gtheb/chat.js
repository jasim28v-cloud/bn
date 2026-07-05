// 💖 VIBE 2026 - Chat & Video Call Module

// ==================== التسجيل الصوتي ====================
async function startVoiceRecording() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];
        mediaRecorder.ondataavailable = (event) => audioChunks.push(event.data);
        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
            const audioUrl = await uploadToCloudinary(audioBlob);
            if (audioUrl && currentChatUser) {
                const chatId = getChatId(currentUser.uid, currentChatUser.uid);
                await db.ref(`chats/${chatId}`).push({
                    senderId: currentUser.uid, audioUrl: audioUrl,
                    timestamp: Date.now(), read: false
                });
                showToast('تم إرسال الرسالة الصوتية');
            }
            stream.getTracks().forEach(track => track.stop());
        };
        mediaRecorder.start();
        isRecording = true;
        document.getElementById('recordingIndicator').style.display = 'flex';
    } catch (error) {
        console.error('Recording error:', error);
        showToast('لا يمكن الوصول إلى الميكروفون');
    }
}

function stopVoiceRecording() {
    if (mediaRecorder && isRecording) {
        mediaRecorder.stop();
        isRecording = false;
        document.getElementById('recordingIndicator').style.display = 'none';
    }
}

function toggleVoiceRecording() { isRecording ? stopVoiceRecording() : startVoiceRecording(); }

// ==================== المحادثات ====================
function onTyping() {
    if (!currentChatUser) return;
    const chatId = getChatId(currentUser.uid, currentChatUser.uid);
    db.ref(`typing/${chatId}/${currentUser.uid}`).set(true);
    if (typingTimeout) clearTimeout(typingTimeout);
    typingTimeout = setTimeout(() => { db.ref(`typing/${chatId}/${currentUser.uid}`).remove(); }, 1000);
}

function listenForTyping(chatId) {
    db.ref(`typing/${chatId}`).on('value', (snapshot) => {
        const typing = snapshot.val();
        const indicator = document.getElementById('typingIndicator');
        if (typing && Object.keys(typing).length > 0 && !typing[currentUser.uid]) {
            indicator.style.display = 'block';
        } else { indicator.style.display = 'none'; }
    });
}

function getChatId(user1, user2) { return [user1, user2].sort().join('_'); }

async function openChat(userId) {
    const s = await db.ref(`users/${userId}`).once('value');
    currentChatUser = s.val();
    
    // 💎 Verified Badge in Chat Header
    const vBadge = currentChatUser.verified ? getVerifiedBadge('sm') : '';
    document.getElementById('chatUserName').innerHTML = `${escapeHtml(currentChatUser.name)} ${vBadge}`;
    document.getElementById('chatAvatar').innerHTML = currentChatUser.avatar ? `<img src="${currentChatUser.avatar}" style="width:100%;height:100%;object-fit:cover">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>';
    const ls = await db.ref(`users/${userId}/lastSeen`).once('value');
    document.getElementById('chatLastSeen').textContent = ls.val() ? `آخر ظهور ${formatTime(ls.val())}` : '';
    const chatId = getChatId(currentUser.uid, userId);
    listenForTyping(chatId);
    await loadChatMessages(userId);
    document.getElementById('chatPanel').classList.add('open');
}

function closeChat() { document.getElementById('chatPanel').classList.remove('open'); if (isRecording) stopVoiceRecording(); currentChatUser = null; }

async function loadChatMessages(userId) {
    const chatId = getChatId(currentUser.uid, userId);
    db.ref(`chats/${chatId}`).off();
    db.ref(`chats/${chatId}`).on('value', (snapshot) => {
        const msgs = snapshot.val();
        const container = document.getElementById('chatMessages');
        if (!container) return;
        if (!msgs) { container.innerHTML = '<div class="text-center p-4 text-gray-500">لا توجد رسائل بعد</div>'; return; }
        let html = '';
        Object.values(msgs).sort((a, b) => a.timestamp - b.timestamp).forEach(msg => {
            const isS = msg.senderId === currentUser.uid;
            html += `<div class="chat-message ${isS ? 'sent' : ''}"><div class="message-bubble ${isS ? 'sent' : ''}">${msg.text ? escapeHtml(msg.text) : ''}${msg.imageUrl ? `<img src="${msg.imageUrl}" class="message-image" onclick="openImageViewer(['${msg.imageUrl}'], 0)">` : ''}${msg.audioUrl ? `<audio controls src="${msg.audioUrl}" style="height: 36px; margin-top: 8px;"></audio>` : ''}</div></div>`;
        });
        container.innerHTML = html;
        container.scrollTop = container.scrollHeight;
    });
}

async function sendChatMessage() {
    const input = document.getElementById('chatMessageInput');
    let text = input?.value;
    if (!text || !currentChatUser) return;
    if (containsBadWords(text)) return showToast('⚠️ تحتوي على كلمات ممنوعة');
    text = filterBadWords(text);
    await db.ref(`chats/${getChatId(currentUser.uid, currentChatUser.uid)}`).push({ senderId: currentUser.uid, text, timestamp: Date.now(), read: false });
    input.value = '';
}

async function sendChatImage(input) {
    const file = input.files[0];
    if (file && currentChatUser) {
        const url = await uploadToCloudinary(file);
        if (url) await db.ref(`chats/${getChatId(currentUser.uid, currentChatUser.uid)}`).push({ senderId: currentUser.uid, imageUrl: url, timestamp: Date.now(), read: false });
    }
    input.value = '';
}

async function openConversations() {
    const cl = document.getElementById('conversationsList');
    cl.innerHTML = '<div class="loading"><div class="spinner"></div></div>';
    const s = await db.ref('chats').once('value');
    const chats = s.val();
    if (!chats) { cl.innerHTML = '<div class="text-center p-4 text-gray-500">لا توجد محادثات</div>'; document.getElementById('conversationsPanel').classList.add('open'); return; }
    const convs = [];
    for (const [cid, msgs] of Object.entries(chats)) {
        const [u1, u2] = cid.split('_');
        const oid = u1 === currentUser.uid ? u2 : u1;
        const us = await db.ref(`users/${oid}`).once('value');
        const ud = us.val();
        const lm = Object.values(msgs).sort((a, b) => b.timestamp - a.timestamp)[0];
        convs.push({ userId: oid, userData: ud, lastMessage: lm, timestamp: lm.timestamp });
    }
    convs.sort((a, b) => b.timestamp - a.timestamp);
    cl.innerHTML = convs.map(c => {
        const vBadge = c.userData?.verified ? getVerifiedBadge('sm') : '';
        return `<div class="follower-item" onclick="closeConversations(); openChat('${c.userId}')"><div class="post-avatar" style="width: 48px; height: 48px;">${c.userData?.avatar ? `<img src="${c.userData.avatar}">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>'}</div><div style="flex: 1;"><div style="font-weight: 600;">${vBadge}${escapeHtml(c.userData?.name || 'مستخدم')}</div><div style="font-size: 12px; color: #8e8e8e;">${c.lastMessage.text ? c.lastMessage.text.substring(0, 30) : (c.lastMessage.audioUrl ? 'رسالة صوتية' : 'صورة')}</div></div></div>`;
    }).join('');
    document.getElementById('conversationsPanel').classList.add('open');
}

function closeConversations() { document.getElementById('conversationsPanel').classList.remove('open'); }

// ==================== مكالمات الفيديو ====================
async function initAgoraCall() {
    if (!agoraClient) agoraClient = AgoraRTC.createClient({ mode: "rtc", codec: "vp8" });
    return agoraClient;
}

async function startVideoCallWithAgora(channelName, userId) {
    try {
        const client = await initAgoraCall();
        await client.join(AGORA_APP_ID_CALL, channelName, null, userId);
        localTracks.videoTrack = await AgoraRTC.createCameraVideoTrack();
        localTracks.audioTrack = await AgoraRTC.createMicrophoneAudioTrack();
        await client.publish([localTracks.videoTrack, localTracks.audioTrack]);
        const localPlayer = document.getElementById('localVideo');
        if (localPlayer) localTracks.videoTrack.play(localPlayer);
        client.on("user-published", async (user, mediaType) => {
            await client.subscribe(user, mediaType);
            if (mediaType === "video") {
                const remotePlayer = document.getElementById('remoteVideo');
                if (remotePlayer) user.videoTrack.play(remotePlayer);
            }
            if (mediaType === "audio") user.audioTrack.play();
        });
        isCallActive = true;
        showToast('تم بدء المكالمة');
    } catch (error) {
        console.error('Video call error:', error);
        showToast('فشل بدء المكالمة');
    }
}

async function endVideoCall() {
    if (agoraClient) {
        if (localTracks.videoTrack) localTracks.videoTrack.close();
        if (localTracks.audioTrack) localTracks.audioTrack.close();
        await agoraClient.leave();
        isCallActive = false;
        showToast('تم إنهاء المكالمة');
    }
    document.getElementById('videoCallModal').classList.remove('open');
}

async function startVideoCallWithCurrentUser() {
    if (!currentChatUser) return;
    const channelName = `call_${getChatId(currentUser.uid, currentChatUser.uid)}`;
    document.getElementById('videoCallModal').classList.add('open');
    await startVideoCallWithAgora(channelName, currentUser.uid);
    await db.ref(`notifications/${currentChatUser.uid}`).push({
        type: 'call', userId: currentUser.uid, userName: currentUser.displayName || currentUser.name,
        channelName: channelName, timestamp: Date.now(), read: false
    });
}

async function startVideoCallWithUser(userId) {
    const channelName = `call_${getChatId(currentUser.uid, userId)}`;
    document.getElementById('videoCallModal').classList.add('open');
    await startVideoCallWithAgora(channelName, currentUser.uid);
    await db.ref(`notifications/${userId}`).push({
        type: 'call', userId: currentUser.uid, userName: currentUser.displayName || currentUser.name,
        channelName: channelName, timestamp: Date.now(), read: false
    });
}

console.log('💖 VIBE Chat Module Ready');
