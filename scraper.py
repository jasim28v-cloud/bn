#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  💖  VIBE 2026 - PREMIUM PINK GLASS EDITION  💖          ║
║     Ultimate Generator - 10 Files - 3000+ Lines            ║
║                                                            ║
║  🔥  Firebase: gomr-3356f                                 ║
║  ☁️   Cloudinary: daemk3hut / fok2_k                       ║
║  👑  Admin: jasim88v@gmail.com                            ║
║  🎥  Agora: 4017f66ea15f4ce088e8d8993a072a5b              ║
║  💖  Design: Premium Pink Glass Transparent               ║
║                                                            ║
║  ✨  PREMIUM FEATURES:                                     ║
║     • 🔔 Notification System (Working 100%)              ║
║     • 🎬 Video Player with Controls                      ║
║     • 🖼️  Image Viewer with Navigation                  ║
║     • 💬 Real-time Chat + Typing Indicators              ║
║     • 🎤 Voice Messages                                  ║
║     • 📊 Polls + Scheduling                              ║
║     • 📌 Pin Posts + Save Posts                          ║
║     • 🔇 Mute/Block/Report System                        ║
║     • 📹 Video Calls (Agora)                             ║
║     • 👁️  Profile Views Tracking                        ║
║     • 🔍 Search Users & Hashtags                         ║
║     • 📖 Read Mode + Hide Likes                          ║
║     • 🌙 Dark Mode Toggle                                ║
║     • 📱 Infinite Scroll Feed                            ║
║     • 🛡️  Admin Panel + Bad Words Filter                ║
║     • 🎀 Premium Pink Glass Design                       ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys

# ═══════════════════════════════════════════════════════════
# 💖 CONFIGURATION - الإعدادات
# ═══════════════════════════════════════════════════════════

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyDqh0Gtl0lIZl8Rt1PvdE67U8yyhjxpJdw",
    "authDomain": "gomr-3356f.firebaseapp.com",
    "databaseURL": "https://gomr-3356f-default-rtdb.firebaseio.com",
    "projectId": "gomr-3356f",
    "storageBucket": "gomr-3356f.firebasestorage.app",
    "messagingSenderId": "470296286364",
    "appId": "1:470296286364:web:2bb6e28a2095757da88959",
    "measurementId": "G-4MLFT3DHJB"
}

CLOUD_NAME = "daemk3hut"
UPLOAD_PRESET = "fok2_k"
AGORA_APP_ID = "4017f66ea15f4ce088e8d8993a072a5b"
ADMIN_EMAIL = "jasim88v@gmail.com"
ADMIN_PASSWORD = "kk2314kk"
SITE_NAME = "VIBE"

# 💖 Premium Pink Glass Palette
PINK_COLORS_JS = """[
    "linear-gradient(135deg, #ec4899, #f472b6, #fbcfe8)",
    "linear-gradient(135deg, #db2777, #ec4899, #f472b6)",
    "linear-gradient(135deg, #be185d, #db2777, #ec4899)",
    "linear-gradient(135deg, #f472b6, #f9a8d4, #fce7f3)",
    "linear-gradient(135deg, #ec4899, #db2777, #be185d)",
    "linear-gradient(135deg, #831843, #be185d, #ec4899)"
]"""

OUTPUT_DIR = "gtheb"

# ═══════════════════════════════════════════════════════════
# 💖 UTILITY - دوال مساعدة
# ═══════════════════════════════════════════════════════════

TOTAL_LINES = 0

def write(filename, content):
    """حفظ ملف وحساب عدد الأسطر"""
    global TOTAL_LINES
    filepath = os.path.join(OUTPUT_DIR, filename)
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else OUTPUT_DIR, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  💖 {filename} ({lines} سطر)")

def section(title):
    """طباعة عنوان القسم"""
    print(f"\n{'='*60}")
    print(f"  💖 {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 💖 1. firebase-config.js
# ═══════════════════════════════════════════════════════════

def build_config():
    return f"""// 💖 VIBE 2026 - Premium Pink Glass Configuration
// Firebase: gomr-3356f | Cloudinary: daemk3hut
// ✨ PREMIUM: Chat + Video Calls + Stories + Polls

const firebaseConfig = {{
    apiKey: "{FIREBASE_CONFIG['apiKey']}",
    authDomain: "{FIREBASE_CONFIG['authDomain']}",
    databaseURL: "{FIREBASE_CONFIG['databaseURL']}",
    projectId: "{FIREBASE_CONFIG['projectId']}",
    storageBucket: "{FIREBASE_CONFIG['storageBucket']}",
    messagingSenderId: "{FIREBASE_CONFIG['messagingSenderId']}",
    appId: "{FIREBASE_CONFIG['appId']}",
    measurementId: "{FIREBASE_CONFIG['measurementId']}"
}};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Services
const auth = firebase.auth();
const db = firebase.database();
const storage = firebase.storage();

// Cloudinary Configuration
const CLOUD_NAME = "{CLOUD_NAME}";
const UPLOAD_PRESET = "{UPLOAD_PRESET}";

// Agora Video Call
const AGORA_APP_ID_CALL = "{AGORA_APP_ID}";

// Admin Account
const ADMIN_EMAIL = '{ADMIN_EMAIL}';
const ADMIN_PASSWORD = '{ADMIN_PASSWORD}';

// 💖 App Info
const APP_NAME = "{SITE_NAME}";
const APP_VERSION = "2026.1";
const PRIMARY_COLOR = "#ec4899";
const SECONDARY_COLOR = "#f472b6";

// 💖 Pink Palette
const PINK_COLORS = {PINK_COLORS_JS};

console.log('💖 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #ec4899; font-size: 18px; font-weight: bold;');
"""

# ═══════════════════════════════════════════════════════════
# 💖 2. auth.html - تسجيل الدخول والاشتراك
# ═══════════════════════════════════════════════════════════

def build_auth():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💖 VIBE | دخول</title>
    <meta name="theme-color" content="#ec4899">
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{
            min-height:100vh;
            background:radial-gradient(ellipse at top, #1a0a1e, #0d0510, #050208);
            display:flex;align-items:center;justify-content:center;
            font-family:'Inter',sans-serif;overflow:hidden;
        }
        .bg-orb{
            position:fixed;border-radius:50%;filter:blur(130px);opacity:0.25;
            animation:orbFloat 20s infinite alternate;
        }
        .bg-orb:nth-child(1){width:400px;height:400px;background:#ec4899;top:-100px;left:-100px}
        .bg-orb:nth-child(2){width:350px;height:350px;background:#f472b6;bottom:-100px;right:-100px;animation-delay:5s}
        .bg-orb:nth-child(3){width:300px;height:300px;background:#fbcfe8;top:50%;left:50%;animation-delay:10s}
        @keyframes orbFloat{0%{transform:translate(0,0) scale(1)}100%{transform:translate(50px,-50px) scale(1.3)}}

        .card{
            position:relative;z-index:1;width:90%;max-width:420px;
            background:rgba(236,72,153,0.03);
            backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);
            border-radius:32px;padding:36px 24px;
            border:1px solid rgba(236,72,153,0.15);
            box-shadow:0 30px 70px rgba(236,72,153,0.08),inset 0 0 30px rgba(236,72,153,0.02);
            animation:fadeUp 0.8s ease;
        }
        @keyframes fadeUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}

        .logo{
            width:70px;height:70px;margin:0 auto 20px;
            background:linear-gradient(135deg, rgba(236,72,153,0.25), rgba(244,114,182,0.25));
            border-radius:20px;display:flex;align-items:center;justify-content:center;
            font-size:36px;border:1px solid rgba(236,72,153,0.15);
            box-shadow:0 15px 40px rgba(236,72,153,0.2);
            animation:logoGlow 3s ease-in-out infinite;
        }
        @keyframes logoGlow{0%,100%{box-shadow:0 15px 40px rgba(236,72,153,0.2)}50%{box-shadow:0 15px 60px rgba(244,114,182,0.5)}}
        h1{text-align:center;font-size:36px;font-weight:900;background:linear-gradient(to bottom, #fff, #fbcfe8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:4px}
        .sub{text-align:center;color:rgba(255,255,255,0.4);font-size:13px;margin-bottom:20px}

        .tabs{display:flex;gap:4px;background:rgba(236,72,153,0.05);border-radius:40px;padding:4px;margin-bottom:24px}
        .tab{flex:1;padding:12px;background:none;border:none;color:rgba(255,255,255,0.5);cursor:pointer;border-radius:40px;font-size:14px;transition:all 0.3s;font-weight:500}
        .tab.active{background:linear-gradient(135deg, #ec4899, #f472b6);color:#fff;box-shadow:0 8px 20px rgba(236,72,153,0.3)}

        .form{display:none;animation:fadeIn 0.4s ease}
        .form.active{display:block}
        @keyframes fadeIn{from{opacity:0}to{opacity:1}}

        input{
            width:100%;padding:15px 18px;margin:8px 0;
            border-radius:50px;background:rgba(236,72,153,0.03);
            border:1px solid rgba(236,72,153,0.12);color:#fff;
            font-size:14px;outline:none;transition:all 0.4s;
        }
        input:focus{border-color:rgba(236,72,153,0.5);box-shadow:0 0 20px rgba(236,72,153,0.08);background:rgba(236,72,153,0.06)}
        input::placeholder{color:rgba(255,255,255,0.3)}

        button{
            width:100%;padding:15px;margin-top:18px;
            background:linear-gradient(135deg, #ec4899, #f472b6);
            border:none;border-radius:50px;color:#fff;
            font-weight:bold;font-size:15px;cursor:pointer;
            transition:all 0.3s;box-shadow:0 10px 30px rgba(236,72,153,0.3);
        }
        button:hover{transform:translateY(-2px);box-shadow:0 20px 40px rgba(236,72,153,0.5)}
        button:active{transform:scale(0.97)}
        button:disabled{opacity:0.5;pointer-events:none}

        .msg{text-align:center;color:#fca5a5;font-size:13px;margin-top:12px;min-height:20px}
        .msg.success{color:#4ade80}
    </style>
</head>
<body>
    <div class="bg-orb"></div><div class="bg-orb"></div><div class="bg-orb"></div>

    <div class="card">
        <div class="logo">💖</div>
        <h1>VIBE</h1>
        <p class="sub">Premium Pink Glass 2026 ✨</p>

        <div class="tabs">
            <button class="tab active" id="tabLogin" onclick="switchTab('login')"><i class="fas fa-sign-in-alt"></i> دخول</button>
            <button class="tab" id="tabRegister" onclick="switchTab('register')"><i class="fas fa-user-plus"></i> اشتراك</button>
        </div>

        <div id="formLogin" class="form active">
            <input type="email" id="loginEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email">
            <input type="password" id="loginPass" placeholder="🔒 كلمة المرور" autocomplete="current-password">
            <button id="btnLogin" onclick="doLogin()"><i class="fas fa-arrow-right-to-bracket"></i> تسجيل الدخول</button>
            <div class="msg" id="loginMsg"></div>
        </div>

        <div id="formRegister" class="form">
            <input type="text" id="regName" placeholder="👤 اسم المستخدم" autocomplete="username">
            <input type="email" id="regEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email">
            <input type="password" id="regPass" placeholder="🔒 كلمة المرور (6 أحرف على الأقل)" autocomplete="new-password">
            <button id="btnRegister" onclick="doRegister()"><i class="fas fa-heart"></i> إنشاء حساب</button>
            <div class="msg" id="regMsg"></div>
        </div>
    </div>

    <script src="firebase-config.js"></script>
    <script>
        function switchTab(type){
            document.getElementById('tabLogin').classList.remove('active');
            document.getElementById('tabRegister').classList.remove('active');
            document.getElementById('formLogin').classList.remove('active');
            document.getElementById('formRegister').classList.remove('active');
            document.getElementById('loginMsg').innerText = '';
            document.getElementById('regMsg').innerText = '';
            if(type === 'login'){
                document.getElementById('tabLogin').classList.add('active');
                document.getElementById('formLogin').classList.add('active');
            } else {
                document.getElementById('tabRegister').classList.add('active');
                document.getElementById('formRegister').classList.add('active');
            }
        }

        async function doLogin(){
            const email = document.getElementById('loginEmail').value.trim();
            const password = document.getElementById('loginPass').value;
            const msg = document.getElementById('loginMsg');
            const btn = document.getElementById('btnLogin');
            if(!email || !password){ msg.innerText = '❌ الرجاء ملء جميع الحقول'; return; }
            btn.disabled = true; btn.innerHTML = '⏳ جاري الدخول...'; msg.innerText = ''; msg.className = 'msg';
            try {
                await auth.signInWithEmailAndPassword(email, password);
                localStorage.setItem('auth_logged_in', 'true');
                window.location.replace('index.html');
            } catch(error) {
                btn.disabled = false; btn.innerHTML = '<i class="fas fa-arrow-right-to-bracket"></i> تسجيل الدخول';
                switch(error.code) {
                    case 'auth/user-not-found': msg.innerText = '❌ لا يوجد حساب بهذا البريد'; break;
                    case 'auth/wrong-password': case 'auth/invalid-credential': msg.innerText = '❌ كلمة المرور غير صحيحة'; break;
                    case 'auth/invalid-email': msg.innerText = '❌ بريد إلكتروني غير صالح'; break;
                    case 'auth/too-many-requests': msg.innerText = '❌ محاولات كثيرة، حاول لاحقاً'; break;
                    default: msg.innerText = '❌ خطأ: ' + error.message;
                }
            }
        }

        async function doRegister(){
            const username = document.getElementById('regName').value.trim();
            const email = document.getElementById('regEmail').value.trim();
            const password = document.getElementById('regPass').value;
            const msg = document.getElementById('regMsg');
            const btn = document.getElementById('btnRegister');
            if(!username || !email || !password){ msg.innerText = '❌ الرجاء ملء جميع الحقول'; return; }
            if(username.length < 3){ msg.innerText = '❌ اسم المستخدم 3 أحرف على الأقل'; return; }
            if(password.length < 6){ msg.innerText = '❌ كلمة المرور 6 أحرف على الأقل'; return; }
            if(!email.includes('@') || !email.includes('.')){ msg.innerText = '❌ بريد إلكتروني غير صالح'; return; }
            btn.disabled = true; btn.innerHTML = '⏳ جاري إنشاء الحساب...'; msg.innerText = ''; msg.className = 'msg';
            try {
                const userCredential = await auth.createUserWithEmailAndPassword(email, password);
                const uid = userCredential.user.uid;
                await db.ref('users/' + uid).set({
                    uid: uid, name: username, email: email, bio: 'مرحباً! أنا في VIBE ✨',
                    avatar: '', cover: '', website: '', verified: false,
                    isAdmin: email === ADMIN_EMAIL, blockedUsers: {}, mutedUntil: 0, createdAt: Date.now()
                });
                msg.innerText = '✅ تم إنشاء الحساب بنجاح! جاري التوجيه...';
                msg.className = 'msg success';
                localStorage.setItem('auth_logged_in', 'true');
                setTimeout(() => { window.location.replace('index.html'); }, 800);
            } catch(error) {
                btn.disabled = false; btn.innerHTML = '<i class="fas fa-heart"></i> إنشاء حساب'; msg.className = 'msg';
                switch(error.code) {
                    case 'auth/email-already-in-use': msg.innerText = '❌ البريد الإلكتروني مستخدم بالفعل'; break;
                    case 'auth/weak-password': msg.innerText = '❌ كلمة المرور ضعيفة جداً'; break;
                    case 'auth/invalid-email': msg.innerText = '❌ بريد إلكتروني غير صالح'; break;
                    default: msg.innerText = '❌ خطأ: ' + (error.message || 'غير معروف');
                }
            }
        }

        document.querySelectorAll('input').forEach(input => {
            input.addEventListener('keydown', function(e) {
                if(e.key === 'Enter') {
                    e.preventDefault();
                    if(document.getElementById('formLogin').classList.contains('active')) { doLogin(); }
                    else { doRegister(); }
                }
            });
        });

        auth.onAuthStateChanged(user => {
            if(user) { window.location.replace('index.html'); }
        });

        console.log('💖 VIBE Auth Ready');
    </script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 💖 3. index.html - الصفحة الرئيسية
# ═══════════════════════════════════════════════════════════

def build_index():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>💖 VIBE | الرئيسية</title>
    <meta name="theme-color" content="#ec4899">
    <link rel="preconnect" href="https://www.gstatic.com">
    <link rel="preconnect" href="https://gomr-3356f-default-rtdb.firebaseio.com">
    <link rel="preconnect" href="https://api.cloudinary.com">
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-storage-compat.js"></script>
    <script src="https://download.agora.io/sdk/release/AgoraRTC_N-4.22.0.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link href="style.css" rel="stylesheet">
</head>
<body>

<div id="initLoader">
    <div class="spinner"></div>
    <div style="margin-top: 16px; color: #ec4899; font-weight: 500;">💖 جاري تحميل VIBE...</div>
</div>

<div id="mainApp">
    <div class="top-bar">
        <div class="logo-vibe" onclick="goToHome()">VIBE</div>
        <div class="top-icons">
            <i class="far fa-comment-dots top-icon" onclick="openConversations()"></i>
            <i class="fas fa-bookmark top-icon" onclick="openSavedPosts()"></i>
            <i class="fas fa-adjust top-icon" onclick="toggleTheme()" id="themeToggle"></i>
            <i class="fas fa-sign-out-alt top-icon" onclick="logout()" style="color: #ec4899;"></i>
        </div>
    </div>

    <div class="main-layout">
        <div id="feedContainer" class="feed-container">
            <div class="loading"><div class="spinner"></div><span>جاري التحميل...</span></div>
        </div>
        <div class="trending-sidebar" id="trendingSidebar">
            <div style="font-weight: 700; margin-bottom: 16px; font-size: 18px;">🔥 الترند</div>
            <div id="trendingList"></div>
            <div style="margin-top: 20px; padding-top: 16px; border-top: 1px solid rgba(236,72,153,0.15);">
                <div style="font-weight: 600; margin-bottom: 12px;">⚙️ الإعدادات السريعة</div>
                <div class="dnd-toggle"><span>📖 وضع القراءة</span><div class="toggle-switch" id="readModeToggle" onclick="toggleReadMode()"></div></div>
                <div class="dnd-toggle"><span>🔕 عدم الإزعاج</span><div class="toggle-switch" id="dndToggle" onclick="toggleDoNotDisturb()"></div></div>
                <div class="dnd-toggle"><span>🔒 إخفاء الإعجابات</span><div class="toggle-switch" id="hideLikesToggle" onclick="toggleHideLikes()"></div></div>
            </div>
        </div>
    </div>

    <div class="bottom-nav">
        <button class="nav-item active" onclick="switchTab('home')"><i class="fas fa-home"></i></button>
        <button class="nav-item" onclick="openSearch()"><i class="fas fa-search"></i></button>
        <button class="nav-item" onclick="openCompose()"><i class="fas fa-plus-square"></i></button>
        <button class="nav-item" onclick="openNotifications()"><i class="far fa-bell"></i></button>
        <button class="nav-item" onclick="openMyProfile()"><i class="fas fa-user-circle"></i></button>
    </div>

    <!-- 💖 Compose Modal -->
    <div id="composeModal" class="compose-modal">
        <div class="compose-content">
            <div class="compose-header"><h3 style="font-weight: 600;">💖 إنشاء منشور جديد</h3><button onclick="closeCompose()" style="background: none; border: none; font-size: 24px; cursor: pointer; color: #fff;">&times;</button></div>
            <div class="compose-area">
                <textarea id="postText" class="compose-textarea" placeholder="اكتب منشوراً..."></textarea>
                <div id="mediaPreview" class="media-preview"></div>
                <div class="quick-emojis">
                    <span onclick="addEmojiToPost('😊')">😊</span><span onclick="addEmojiToPost('😂')">😂</span><span onclick="addEmojiToPost('❤️')">❤️</span>
                    <span onclick="addEmojiToPost('🔥')">🔥</span><span onclick="addEmojiToPost('🎉')">🎉</span><span onclick="addEmojiToPost('😢')">😢</span>
                    <span onclick="addEmojiToPost('😮')">😮</span><span onclick="openStickerPicker()">😀</span>
                </div>
                <div id="stickerPicker" class="sticker-picker"></div>
                <div class="compose-tools">
                    <button class="compose-tool" onclick="document.getElementById('postImage').click()"><i class="fas fa-image"></i></button>
                    <button class="compose-tool" onclick="document.getElementById('postVideo').click()"><i class="fas fa-video"></i></button>
                    <button class="compose-tool" onclick="addPollToCompose()"><i class="fas fa-chart-bar"></i></button>
                    <button class="compose-tool" onclick="toggleSchedulePicker()"><i class="fas fa-calendar-alt"></i></button>
                </div>
                <div id="schedulePicker" class="schedule-picker">
                    <input type="datetime-local" id="scheduleDate" class="chat-input" style="width: 100%;">
                    <button onclick="schedulePost()" style="margin-top: 8px; background: linear-gradient(135deg, #ec4899, #f472b6); color: white; border: none; padding: 8px; border-radius: 12px; width: 100%;">جدولة النشر</button>
                </div>
                <div id="pollBuilder" style="display: none; margin-top: 12px;">
                    <input type="text" id="pollQuestion" placeholder="سؤال التصويت..." class="chat-input" style="width: 100%; margin-bottom: 8px;">
                    <input type="text" id="pollOption1" placeholder="خيار 1" class="chat-input" style="width: 100%; margin-bottom: 4px;">
                    <input type="text" id="pollOption2" placeholder="خيار 2" class="chat-input" style="width: 100%; margin-bottom: 4px;">
                    <button onclick="addPollOption()" style="background: none; border: 1px solid #ec4899; color: #ec4899; padding: 4px 8px; border-radius: 8px;">+ إضافة خيار</button>
                </div>
                <input type="file" id="postImage" accept="image/*" style="display:none" onchange="previewMedia(this, 'image')">
                <input type="file" id="postVideo" accept="video/*" style="display:none" onchange="previewMedia(this, 'video')">
                <button id="publishPostBtn" onclick="createPost()" style="width: 100%; background: linear-gradient(135deg, #ec4899, #f472b6); color: white; padding: 12px; border-radius: 12px; margin-top: 16px; font-weight: 600; border: none; cursor: pointer;">💖 مشاركة</button>
            </div>
        </div>
    </div>

    <!-- 💖 Panels -->
    <div id="commentsPanel" class="chat-panel">
        <div class="chat-header"><h3 style="font-weight: 600;">💬 التعليقات</h3><button onclick="closeComments()" style="background: none; border: none; font-size: 24px; cursor: pointer; color: #fff;">&times;</button></div>
        <div id="commentsList" class="chat-messages"></div>
        <div class="chat-input-area"><input type="text" id="commentInput" class="chat-input" placeholder="أضف تعليقاً..."><button onclick="addComment()" class="chat-send-btn"><i class="fas fa-paper-plane"></i></button></div>
    </div>

    <div id="profilePanel" class="chat-panel">
        <div class="chat-header"><h3 style="font-weight: 600;">💖 الملف الشخصي</h3><button onclick="closeProfile()" style="background: none; border: none; font-size: 24px; cursor: pointer; color: #fff;">&times;</button></div>
        <div style="overflow-y: auto;">
            <div id="profileCover" class="profile-cover"></div>
            <div class="profile-avatar-wrapper"><div class="profile-avatar-large" id="profileAvatarLarge"><i class="fas fa-user text-5xl text-white flex items-center justify-center h-full"></i></div></div>
            <div class="profile-info">
                <div class="profile-name" id="profileName"></div>
                <div class="profile-bio" id="profileBio"></div>
                <div id="profileWebsite" class="profile-bio" style="color: #ec4899;"></div>
                <div class="profile-stats">
                    <div class="stat-item" onclick="openFollowersList('followers')"><div class="stat-number" id="profileFollowersCount">0</div><div>متابع</div></div>
                    <div class="stat-item" onclick="openFollowersList('following')"><div class="stat-number" id="profileFollowingCount">0</div><div>يتابع</div></div>
                    <div class="stat-item"><div class="stat-number" id="profilePostsCount">0</div><div>منشورات</div></div>
                    <div class="stat-item" onclick="openProfileViews()"><div class="stat-number" id="profileViewsCount">0</div><div>مشاهدة</div></div>
                </div>
                <div id="profileButtons" class="profile-buttons"></div>
            </div>
            <div class="profile-tabs">
                <button class="profile-tab active" onclick="loadProfilePosts(currentProfileUser)"><i class="fas fa-table-cells-large"></i> المنشورات</button>
                <button class="profile-tab" onclick="loadProfileMedia(currentProfileUser)"><i class="fas fa-clapperboard"></i> الوسائط</button>
                <button class="profile-tab" onclick="openSavedPosts()"><i class="fas fa-bookmark"></i> المحفوظة</button>
            </div>
            <div id="profilePostsGrid" class="profile-grid"></div>
        </div>
    </div>

    <div id="editProfileModal" class="modal-overlay">
        <div class="modal-content"><div style="text-align: center; margin-bottom: 20px;"><h3 style="font-weight: 600;">💖 تعديل الملف الشخصي</h3></div>
        <input type="text" id="editName" class="chat-input" style="width: 100%; margin-bottom: 12px;" placeholder="الاسم">
        <textarea id="editBio" class="chat-input" style="width: 100%; min-height: 80px; margin-bottom: 12px;" placeholder="السيرة الذاتية..."></textarea>
        <input type="url" id="editWebsite" class="chat-input" style="width: 100%; margin-bottom: 12px;" placeholder="رابط الموقع">
        <div style="display: flex; gap: 10px;"><button class="profile-btn" onclick="closeEditProfileModal()">إلغاء</button><button class="profile-btn profile-btn-primary" onclick="saveProfileEdit()">💖 حفظ</button></div></div>
    </div>

    <div id="chatPanel" class="chat-panel">
        <div class="chat-header"><div style="display: flex; align-items: center; gap: 12px;"><div class="profile-avatar-large" id="chatAvatar" style="width: 40px; height: 40px;"></div><div><h3 id="chatUserName" style="font-weight: 600;">محادثة</h3><div id="chatLastSeen" class="last-seen"></div></div></div><div style="display: flex; gap: 12px;"><button class="chat-send-btn" onclick="startVideoCallWithCurrentUser()" style="color: #ec4899;"><i class="fas fa-video"></i></button><button onclick="closeChat()" style="background: none; border: none; font-size: 24px; cursor: pointer; color: #fff;">&times;</button></div></div>
        <div id="chatMessages" class="chat-messages"></div>
        <div id="typingIndicator" class="typing-indicator" style="display: none;">✏️ جاري الكتابة...</div>
        <div class="chat-input-area"><div id="recordingIndicator" class="recording-indicator" style="display: none;"><span>جاري التسجيل...</span></div><button class="chat-audio-btn" onclick="toggleVoiceRecording()"><i class="fas fa-microphone"></i></button><input type="file" id="chatImageInput" accept="image/*" style="display:none" onchange="sendChatImage(this)"><button class="chat-image-btn" onclick="document.getElementById('chatImageInput').click()"><i class="fas fa-image"></i></button><input type="text" id="chatMessageInput" class="chat-input" placeholder="اكتب رسالة..." onkeyup="onTyping()"><button class="chat-send-btn" onclick="sendChatMessage()"><i class="fas fa-paper-plane"></i></button></div>
    </div>

    <div id="conversationsPanel" class="chat-panel"><div class="chat-header"><h3 style="font-weight: 600;">💌 الرسائل</h3><button onclick="closeConversations()" style="background: none; border: none; font-size: 24px; cursor: pointer; color: #fff;">&times;</button></div><div id="conversationsList" style="padding: 12px;"></div></div>
    <div id="followersPanel" class="chat-panel"><div class="chat-header"><h3 id="followersTitle" style="font-weight: 600;">المتابعون</h3><button onclick="closeFollowers()" style="background: none; border: none; font-size: 24px; cursor: pointer; color: #fff;">&times;</button></div><div id="followersList" style="padding: 12px;"></div></div>
    <div id="notificationsPanel" class="chat-panel"><div class="chat-header"><h3 style="font-weight: 600;">🔔 الإشعارات</h3><button onclick="closeNotifications()" style="background: none; border: none; font-size: 24px; cursor: pointer; color: #fff;">&times;</button></div><div id="notificationsList" style="padding: 12px;"></div></div>
    <div id="searchPanel" class="chat-panel"><div class="chat-header"><h3 style="font-weight: 600;">🔍 بحث</h3><button onclick="closeSearch()" style="background: none; border: none; font-size: 24px; cursor: pointer; color: #fff;">&times;</button></div><input type="text" id="searchInput" class="chat-input" style="margin: 12px; width: calc(100% - 24px);" placeholder="بحث عن مستخدمين أو هاشتاجات..." onkeyup="searchAll()"><div id="searchResults" style="padding: 12px;"></div></div>
    
    <div id="savedPostsPanel" class="chat-panel"><div class="chat-header"><h3 style="font-weight: 600;">📌 المنشورات المحفوظة</h3><button onclick="closeSavedPosts()" style="background: none; border: none; font-size: 24px; cursor: pointer; color: #fff;">&times;</button></div><div id="savedPostsGrid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2px; padding: 8px;"></div></div>
    <div id="profileViewsPanel" class="chat-panel"><div class="chat-header"><h3 style="font-weight: 600;">👁️ من شاهد ملفك</h3><button onclick="closeProfileViews()" style="background: none; border: none; font-size: 24px; cursor: pointer; color: #fff;">&times;</button></div><div id="profileViewsList" style="padding: 12px;"></div></div>

    <div id="reportModal" class="modal-overlay">
        <div class="modal-content"><h3 style="font-weight: 600; margin-bottom: 16px;">🚨 الإبلاغ</h3>
        <div id="reportReasons"><div class="report-reason" onclick="selectReportReason(this, 'محتوى غير لائق')">محتوى غير لائق</div><div class="report-reason" onclick="selectReportReason(this, 'تحرش')">تحرش</div><div class="report-reason" onclick="selectReportReason(this, 'عنف')">عنف</div><div class="report-reason" onclick="selectReportReason(this, 'سب وقذف')">سب وقذف</div><div class="report-reason" onclick="selectReportReason(this, 'معلومات مضللة')">معلومات مضللة</div></div>
        <button class="profile-btn profile-btn-primary" onclick="submitReport()" style="margin-top: 16px; width: 100%;">إرسال</button><button class="profile-btn" onclick="closeReportModal()" style="width: 100%; margin-top: 8px;">إلغاء</button></div>
    </div>

    <div id="imageViewerModal" class="image-viewer-modal" onclick="closeImageViewer()">
        <div class="image-viewer-close" onclick="closeImageViewer()">&times;</div>
        <button class="image-viewer-prev" onclick="event.stopPropagation(); prevImage()">&#10094;</button>
        <img id="viewerImage" src="">
        <button class="image-viewer-next" onclick="event.stopPropagation(); nextImage()">&#10095;</button>
    </div>

    <div id="videoCallModal" class="video-call-modal">
        <div class="video-container"><div id="remoteVideo"></div><div id="localVideo"></div></div>
        <div class="call-controls"><button class="call-end-btn" onclick="endVideoCall()"><i class="fas fa-phone-slash"></i></button></div>
    </div>

    <!-- 💖 Admin Panel -->
    <div id="adminPanel" class="admin-panel">
        <div class="chat-header"><h3 style="font-weight: 600;">💖 لوحة التحكم</h3><button onclick="closeAdmin()" style="background: none; border: none; font-size: 24px; cursor: pointer; color: #fff;">&times;</button></div>
        <div class="admin-stats"><div class="admin-stat-card"><div class="admin-stat-number" id="adminUsersCount">0</div><div>مستخدمين</div></div><div class="admin-stat-card"><div class="admin-stat-number" id="adminPostsCount">0</div><div>منشورات</div></div><div class="admin-stat-card"><div class="admin-stat-number" id="adminCommentsCount">0</div><div>تعليقات</div></div></div>
        <div style="padding: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <h4 style="font-weight: 600;"><i class="fas fa-ban"></i> 🚫 الكلمات الممنوعة</h4>
                <button onclick="showAddBadWordModal()" style="background: linear-gradient(135deg, #ec4899, #f472b6); color: white; border: none; padding: 6px 12px; border-radius: 8px; cursor: pointer; font-size: 12px;">+ إضافة كلمة</button>
            </div>
            <div id="badWordsList" style="margin-bottom: 20px;"></div>
        </div>
        <div style="padding: 16px;">
            <h4 style="font-weight: 600; margin-bottom: 12px;"><i class="fas fa-users"></i> إدارة المستخدمين</h4>
            <div id="adminUsersList"></div>
        </div>
        <div style="padding: 16px;">
            <h4 style="font-weight: 600; margin-bottom: 12px;"><i class="fas fa-newspaper"></i> أحدث المنشورات</h4>
            <div id="adminPostsList"></div>
        </div>
    </div>
</div>

<div id="customToast"></div>

<script src="firebase-config.js"></script>
<script src="script.js"></script>

</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 💖 4. style.css - التنسيقات الكاملة
# ═══════════════════════════════════════════════════════════

def build_style():
    return """/* 💖 VIBE 2026 - Premium Pink Glass Theme */
:root {
    --pink: #ec4899;
    --pink-light: #f472b6;
    --pink-pale: #fbcfe8;
    --pink-dark: #be185d;
    --pink-deep: #831843;
    --bg-light: #fafafa;
    --bg-dark: #0a0a0a;
    --text-light: #262626;
    --text-dark: #ffffff;
    --glass: rgba(236, 72, 153, 0.05);
    --glass-border: rgba(236, 72, 153, 0.15);
    --glass-hover: rgba(236, 72, 153, 0.1);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Inter', sans-serif;
    background: var(--bg-light);
    color: var(--text-light);
    overflow-x: hidden;
    min-height: 100vh;
}

body.dark-mode { background: var(--bg-dark); color: var(--text-dark); }
body.dark-mode .post-card { background: #0d0d0d; border-bottom-color: #1a1a1a; }
body.dark-mode .top-bar { background: rgba(10,10,10,0.9); border-bottom-color: #1a1a1a; }
body.dark-mode .bottom-nav { background: rgba(10,10,10,0.95); border-top-color: #1a1a1a; }
body.dark-mode .chat-panel { background: #0d0d0d; }
body.dark-mode .message-bubble { background: #1a1a1a; color: white; }
body.dark-mode .compose-content { background: #0d0d0d; border: 1px solid var(--glass-border); }
body.dark-mode .trending-sidebar { background: #0d0d0d; border-left-color: #1a1a1a; }
body.dark-mode .poll-container { background: #1a1a1a; }
body.dark-mode .poll-option { background: #222; }
body.dark-mode .quote-post { background: #1a1a1a; }
body.dark-mode .top-icon, body.dark-mode .post-action, body.dark-mode .nav-item { color: #ffffff; }

/* Animations */
@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@keyframes spin { to { transform: rotate(360deg); } }
@keyframes pinkGlow { 0% { text-shadow: 0 0 0px var(--pink); } 50% { text-shadow: 0 0 20px var(--pink); } 100% { text-shadow: 0 0 0px var(--pink); } }
@keyframes heartFloat { 0% { transform: scale(0.5) translateY(0); opacity: 1; } 100% { transform: scale(1.5) translateY(-50px); opacity: 0; } }
@keyframes btnPress { 0% { transform: scale(1); } 50% { transform: scale(0.95); } 100% { transform: scale(1); } }

.fade-in { animation: fadeIn 0.3s ease-out; }
.post-card { animation: fadeIn 0.2s ease-out; transition: transform 0.15s; cursor: pointer; }
.post-card:active { transform: scale(0.99); }
.post-card.pinned { border-right: 3px solid var(--pink); }

button, .nav-item, .post-action, .profile-btn, .stat-item, .trending-item, .follower-item {
    touch-action: manipulation;
    transition: transform 0.1s;
}
button:active, .nav-item:active, .post-action:active, .profile-btn:active {
    transform: scale(0.95);
}

/* Logo */
.logo-vibe {
    font-size: 28px;
    font-weight: 800;
    background: linear-gradient(135deg, var(--pink), var(--pink-light));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    cursor: pointer;
    animation: pinkGlow 2s infinite;
}

/* Spinner */
.spinner {
    width: 32px;
    height: 32px;
    border: 2px solid rgba(236,72,153,0.2);
    border-top-color: var(--pink);
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
    margin: 0 auto 12px;
}

/* Top Bar */
.top-bar {
    position: sticky;
    top: 0;
    background: rgba(250,250,250,0.9);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(236,72,153,0.1);
    padding: 12px 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 100;
}
.top-icons { display: flex; gap: 22px; align-items: center; }
.top-icon { font-size: 24px; color: #262626; cursor: pointer; transition: transform 0.1s; }
.top-icon:active { transform: scale(0.95); }

/* Layout */
.main-layout { display: flex; max-width: 1200px; margin: 0 auto; }
.feed-container { flex: 1; max-width: 600px; margin: 0 auto; padding: 0 0 20px; }
.trending-sidebar {
    width: 280px;
    position: sticky;
    top: 70px;
    height: calc(100vh - 70px);
    overflow-y: auto;
    padding: 16px;
    background: #ffffff;
    border-left: 1px solid rgba(236,72,153,0.1);
    margin-right: 20px;
    border-radius: 16px;
    display: none;
}
@media (min-width: 1024px) { .trending-sidebar { display: block; } }

/* Bottom Nav */
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(250,250,250,0.95);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-top: 1px solid rgba(236,72,153,0.1);
    display: flex;
    justify-content: space-around;
    padding: 8px 0 12px;
    z-index: 100;
}
.nav-item { background: none; border: none; font-size: 24px; color: #262626; cursor: pointer; padding: 6px; }
.nav-item.active { color: var(--pink); }

/* Post Card */
.post-card { background: #ffffff; border-bottom: 1px solid rgba(236,72,153,0.08); margin-bottom: 0; position: relative; }
.pinned-badge {
    position: absolute; top: 12px; left: 12px;
    background: var(--pink); color: white;
    padding: 4px 8px; border-radius: 20px;
    font-size: 10px; font-weight: 600; z-index: 10;
}
.post-header { display: flex; align-items: center; justify-content: space-between; padding: 12px 16px; }
.post-user-info { display: flex; align-items: center; gap: 12px; cursor: pointer; }
.post-avatar { width: 40px; height: 40px; border-radius: 50%; overflow: hidden; background: linear-gradient(135deg, var(--pink), var(--pink-light)); }
.post-avatar img { width: 100%; height: 100%; object-fit: cover; }
.post-username { font-weight: 600; font-size: 14px; display: flex; align-items: center; gap: 4px; }
.post-time { font-size: 10px; color: #8e8e8e; margin-top: 2px; }
.post-menu { background: none; border: none; font-size: 18px; cursor: pointer; color: #262626; transition: transform 0.1s; }
body.dark-mode .post-menu { color: #ffffff; }
.post-menu:active { transform: scale(0.9); }

.post-actions { display: flex; gap: 20px; padding: 8px 16px; }
.post-action { background: none; border: none; font-size: 24px; cursor: pointer; color: #262626; }
.post-action.active { color: var(--pink); }
.post-likes { font-weight: 600; font-size: 14px; padding: 0 16px 4px; }
.post-caption { padding: 0 16px 8px; font-size: 14px; }
.post-caption span { font-weight: 600; cursor: pointer; }
.post-hashtags { color: var(--pink); cursor: pointer; }
.post-comments { padding: 0 16px 8px; font-size: 14px; color: #8e8e8e; cursor: pointer; }
.post-views { padding: 0 16px 8px; font-size: 11px; color: #8e8e8e; }

.post-image { width: 100%; max-height: 500px; object-fit: cover; cursor: pointer; border-radius: 4px; }

/* Video */
.video-container { position: relative; background: #000; border-radius: 16px; overflow: hidden; margin: 12px 0; }
.post-video { width: 100%; max-height: 500px; object-fit: cover; cursor: pointer; }
.video-controls {
    position: absolute; bottom: 10px; right: 10px;
    background: rgba(0,0,0,0.6); backdrop-filter: blur(4px);
    border-radius: 30px; padding: 6px 12px;
    display: flex; gap: 12px; opacity: 0; transition: opacity 0.3s; pointer-events: none;
}
.video-container:hover .video-controls { opacity: 1; pointer-events: auto; }
.video-controls button { background: none; border: none; color: white; font-size: 16px; cursor: pointer; padding: 4px; }
.video-controls button:hover { color: var(--pink); }

/* Panels */
.chat-panel {
    position: fixed; inset: 0; background: #ffffff; z-index: 400;
    transform: translateX(100%); transition: 0.25s;
    display: flex; flex-direction: column;
}
.chat-panel.open { transform: translateX(0); }
body.dark-mode .chat-panel { background: #0d0d0d; }

.chat-header { padding: 12px 16px; border-bottom: 1px solid rgba(236,72,153,0.1); display: flex; justify-content: space-between; align-items: center; }
.chat-messages { flex: 1; overflow-y: auto; padding: 16px; display: flex; flex-direction: column; gap: 12px; }
.chat-message { display: flex; gap: 8px; max-width: 80%; }
.chat-message.sent { align-self: flex-end; flex-direction: row-reverse; }
.message-bubble { background: #f3f3f3; padding: 10px 14px; border-radius: 20px; font-size: 14px; }
.message-bubble.sent { background: linear-gradient(135deg, var(--pink), var(--pink-light)); color: white; }
.message-status { font-size: 10px; color: #8e8e8e; margin-top: 4px; }

.chat-input-area { display: flex; gap: 12px; padding: 12px; border-top: 1px solid rgba(236,72,153,0.1); align-items: center; }
.chat-input { flex: 1; padding: 10px 14px; border: 1px solid rgba(236,72,153,0.15); border-radius: 25px; outline: none; font-size: 14px; background: transparent; color: inherit; }
.chat-send-btn, .chat-image-btn, .chat-audio-btn { background: none; border: none; font-size: 22px; cursor: pointer; color: var(--pink); transition: transform 0.1s; }
.chat-send-btn:active, .chat-image-btn:active, .chat-audio-btn:active { transform: scale(0.9); }

/* Compose */
.compose-modal { position: fixed; inset: 0; background: rgba(0,0,0,0.9); z-index: 200; display: flex; align-items: center; justify-content: center; opacity: 0; visibility: hidden; transition: 0.2s; }
.compose-modal.open { opacity: 1; visibility: visible; }
.compose-content { background: #ffffff; border-radius: 20px; width: 90%; max-width: 500px; max-height: 80vh; overflow-y: auto; }
.compose-header { display: flex; justify-content: space-between; align-items: center; padding: 16px; border-bottom: 1px solid rgba(236,72,153,0.1); }
.compose-area { padding: 16px; }
.compose-textarea { width: 100%; min-height: 120px; border: none; resize: none; font-size: 16px; outline: none; font-family: inherit; background: transparent; color: inherit; }
.media-preview { margin: 12px 0; display: none; position: relative; }
.media-preview img, .media-preview video { max-height: 250px; border-radius: 12px; width: 100%; object-fit: cover; }
.compose-tools { display: flex; gap: 16px; padding: 12px 0; border-top: 1px solid rgba(236,72,153,0.1); }
.compose-tool { background: none; border: none; font-size: 24px; cursor: pointer; color: #262626; transition: transform 0.1s; }
body.dark-mode .compose-tool { color: #ffffff; }
.compose-tool:active { transform: scale(0.95); }

/* Profile */
.profile-cover {
    width: 100%; height: 200px;
    background: linear-gradient(135deg, var(--pink), var(--pink-light));
    background-size: cover; background-position: center; cursor: pointer;
}
.profile-avatar-wrapper { position: relative; margin-top: -60px; padding: 0 16px; }
.profile-avatar-large {
    width: 120px; height: 120px; border-radius: 50%; overflow: hidden;
    border: 4px solid #ffffff;
    background: linear-gradient(135deg, var(--pink), var(--pink-light)); cursor: pointer;
}
body.dark-mode .profile-avatar-large { border-color: #0d0d0d; }
.profile-info { padding: 12px 16px 16px; }
.profile-name { font-size: 20px; font-weight: 700; display: flex; align-items: center; gap: 6px; }
.verified-badge { color: var(--pink); font-size: 18px; }
.profile-bio { font-size: 14px; color: #8e8e8e; margin-top: 4px; }
.profile-stats { display: flex; gap: 30px; margin-top: 12px; padding: 12px 0; border-top: 1px solid rgba(236,72,153,0.1); border-bottom: 1px solid rgba(236,72,153,0.1); }
.stat-item { text-align: center; cursor: pointer; }
.stat-number { font-weight: 700; font-size: 18px; }
.profile-buttons { display: flex; gap: 10px; margin-top: 16px; flex-wrap: wrap; }
.profile-btn { flex: 1; padding: 8px; border-radius: 8px; font-weight: 600; font-size: 14px; cursor: pointer; border: 1px solid rgba(236,72,153,0.2); background: none; color: inherit; }
.profile-btn-primary { background: linear-gradient(135deg, var(--pink), var(--pink-light)); color: white; border: none; }
.profile-tabs { display: flex; margin-top: 8px; }
.profile-tab { flex: 1; text-align: center; padding: 12px; cursor: pointer; font-size: 14px; font-weight: 600; color: #8e8e8e; background: none; border: none; }
.profile-tab.active { color: var(--pink); border-bottom: 2px solid var(--pink); }
.profile-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2px; margin-top: 4px; }
.grid-item { aspect-ratio: 1; overflow: hidden; cursor: pointer; background: #f5f5f5; position: relative; }
.grid-item:active { transform: scale(0.98); }
.grid-item img, .grid-item video { width: 100%; height: 100%; object-fit: cover; }
.grid-item-overlay {
    position: absolute; bottom: 0; left: 0; right: 0;
    background: rgba(0,0,0,0.6); color: white;
    display: flex; justify-content: center; gap: 16px; padding: 4px; font-size: 12px;
}

/* Modals */
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.9); z-index: 600; display: flex; align-items: center; justify-content: center; opacity: 0; visibility: hidden; transition: 0.2s; }
.modal-overlay.open { opacity: 1; visibility: visible; }
.modal-content { background: #ffffff; border-radius: 20px; padding: 24px; width: 90%; max-width: 400px; }
body.dark-mode .modal-content { background: #0d0d0d; }

/* Image Viewer */
.image-viewer-modal { position: fixed; inset: 0; background: rgba(0,0,0,0.95); z-index: 1000; display: flex; align-items: center; justify-content: center; opacity: 0; visibility: hidden; transition: 0.2s; }
.image-viewer-modal.open { opacity: 1; visibility: visible; }
.image-viewer-modal img { max-width: 90%; max-height: 90%; object-fit: contain; border-radius: 16px; }
.image-viewer-close { position: absolute; top: 20px; right: 20px; font-size: 32px; color: white; cursor: pointer; }
.image-viewer-prev, .image-viewer-next { position: absolute; top: 50%; transform: translateY(-50%); background: rgba(0,0,0,0.5); color: white; border: none; font-size: 32px; cursor: pointer; width: 50px; height: 50px; border-radius: 50%; }
.image-viewer-prev { left: 20px; }
.image-viewer-next { right: 20px; }

/* Video Call */
.video-call-modal { position: fixed; inset: 0; background: #000; z-index: 700; display: flex; flex-direction: column; opacity: 0; visibility: hidden; }
.video-call-modal.open { opacity: 1; visibility: visible; }
.video-container { flex: 1; display: flex; flex-direction: column; position: relative; }
#remoteVideo { flex: 1; background: #000; }
#localVideo { width: 120px; height: 180px; position: absolute; bottom: 20px; right: 20px; background: #333; border-radius: 16px; border: 2px solid white; }
.call-controls { padding: 20px; display: flex; justify-content: center; }
.call-end-btn { background: var(--pink); color: white; border: none; width: 60px; height: 60px; border-radius: 50%; font-size: 24px; cursor: pointer; }

/* Poll */
.poll-container { background: #f5f5f5; border-radius: 16px; padding: 12px; margin: 12px 0; }
.poll-option { background: white; border-radius: 12px; padding: 10px; margin: 8px 0; cursor: pointer; transition: 0.15s; position: relative; overflow: hidden; }
.poll-option:hover { background: rgba(236,72,153,0.15); }
.poll-option.selected { background: var(--pink); color: white; }
.poll-progress { position: absolute; left: 0; top: 0; height: 100%; background: rgba(236,72,153,0.2); transition: width 0.2s; z-index: 0; }
.poll-option-text { position: relative; z-index: 1; display: flex; justify-content: space-between; }

/* Quote */
.quote-post { background: #f5f5f5; border-radius: 16px; padding: 12px; margin: 8px 0; border-right: 4px solid var(--pink); }

/* Toggle Switch */
.toggle-switch { width: 50px; height: 24px; background: #dbdbdb; border-radius: 24px; cursor: pointer; position: relative; transition: 0.15s; }
.toggle-switch.active { background: var(--pink); }
.toggle-switch::after { content: ''; width: 20px; height: 20px; background: white; border-radius: 50%; position: absolute; top: 2px; left: 4px; transition: 0.15s; }
.toggle-switch.active::after { left: 26px; }
.dnd-toggle { background: rgba(236,72,153,0.03); border-radius: 12px; margin-top: 8px; display: flex; justify-content: space-between; padding: 12px; border: 1px solid rgba(236,72,153,0.1); }

/* Toast */
#customToast {
    position: fixed; bottom: 80px; left: 50%; transform: translateX(-50%);
    background: #262626; color: white; padding: 10px 20px; border-radius: 40px;
    z-index: 1100; font-size: 13px; opacity: 0; transition: 0.2s;
    pointer-events: none; white-space: nowrap;
}

/* Heart Animation */
.heart-animation { position: fixed; font-size: 48px; color: var(--pink); pointer-events: none; z-index: 1000; animation: heartFloat 0.6s ease-out forwards; }

/* Admin */
.admin-panel { position: fixed; inset: 0; background: #ffffff; z-index: 500; transform: translateX(100%); transition: 0.25s; overflow-y: auto; }
.admin-panel.open { transform: translateX(0); }
body.dark-mode .admin-panel { background: #0d0d0d; }
.admin-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; padding: 16px; }
.admin-stat-card { background: linear-gradient(135deg, var(--pink), var(--pink-light)); padding: 16px; border-radius: 16px; text-align: center; color: white; }
.admin-item { display: flex; justify-content: space-between; align-items: center; padding: 12px; border-bottom: 1px solid rgba(236,72,153,0.1); }

/* Init Loader */
#initLoader { position: fixed; inset: 0; background: #fafafa; z-index: 9999; display: flex; align-items: center; justify-content: center; flex-direction: column; transition: opacity 0.3s; }
body.dark-mode #initLoader { background: var(--bg-dark); }

#mainApp { display: none; min-height: 100vh; padding-bottom: 70px; }

.loading { text-align: center; padding: 60px 20px; }
.load-more-btn { text-align: center; padding: 16px; margin: 16px; background: rgba(236,72,153,0.05); border-radius: 30px; cursor: pointer; transition: 0.15s; border: 1px solid rgba(236,72,153,0.1); }
.load-more-btn:active { transform: scale(0.98); }
body.dark-mode .load-more-btn { background: #1a1a1a; color: white; }

.quick-emojis { display: flex; gap: 8px; padding: 8px 0; }
.quick-emojis span { font-size: 20px; cursor: pointer; }
.sticker-picker { display: none; grid-template-columns: repeat(4, 1fr); gap: 8px; padding: 12px 0; }
.sticker-picker span { font-size: 28px; cursor: pointer; }

.trending-item { padding: 12px; border-bottom: 1px solid rgba(236,72,153,0.08); cursor: pointer; transition: 0.15s; }
.trending-item:hover { background: rgba(236,72,153,0.05); border-radius: 12px; }
.trending-hashtag { font-weight: 600; color: var(--pink); }

.follower-item { display: flex; align-items: center; gap: 12px; padding: 12px; cursor: pointer; transition: 0.15s; border-bottom: 1px solid rgba(236,72,153,0.08); }
.follower-item:active { transform: scale(0.98); }
.follower-item:hover { background: rgba(236,72,153,0.03); }

.last-seen { font-size: 10px; color: #8e8e8e; margin-top: 2px; }
.typing-indicator { font-size: 12px; color: #8e8e8e; padding: 8px 16px; font-style: italic; }
.recording-indicator { background: var(--pink); color: white; padding: 8px 16px; border-radius: 40px; font-size: 12px; }

.notification-badge {
    position: absolute; top: -6px; right: -10px;
    background: var(--pink); color: white; font-size: 9px;
    border-radius: 50%; width: 16px; height: 16px;
    display: flex; align-items: center; justify-content: center;
}

.report-reason { padding: 10px; margin: 5px 0; background: rgba(236,72,153,0.05); border-radius: 8px; cursor: pointer; transition: 0.1s; border: 1px solid rgba(236,72,153,0.1); }
.report-reason:active { transform: scale(0.98); }
.report-reason.selected { background: var(--pink); color: white; }

.message-image { max-width: 200px; border-radius: 12px; margin-top: 8px; cursor: pointer; }
.schedule-picker { display: none; margin-top: 12px; padding: 12px; background: rgba(236,72,153,0.03); border-radius: 12px; border: 1px solid rgba(236,72,153,0.1); }
"""

# ═══════════════════════════════════════════════════════════
# 💖 5. script.js - الجافاسكريبت الكامل
# ═══════════════════════════════════════════════════════════

def build_script():
    return """// 💖 VIBE 2026 - Premium Pink Glass Edition
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

// ==================== الكلمات الممنوعة ====================
async function loadBadWordsList() {
    const snapshot = await db.ref('badWords').once('value');
    const words = snapshot.val();
    badWordsList = words ? Object.values(words) : [];
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

// ==================== المنشورات ====================
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

function createHeartAnimation(x, y) {
    const heart = document.createElement('div');
    heart.className = 'heart-animation';
    heart.innerHTML = '❤️';
    heart.style.left = x + 'px';
    heart.style.top = y + 'px';
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 600);
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
            html += `<div class="follower-item" onclick="closeProfileViews(); openProfile('${view.viewerId}')">
                <div class="post-avatar" style="width: 44px; height: 44px;">${view.viewerAvatar ? `<img src="${view.viewerAvatar}">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>'}</div>
                <div><div style="font-weight: 600;">${escapeHtml(view.viewerName)}</div><div style="font-size: 11px; color: #8e8e8e;">${formatTime(view.timestamp)}</div></div>
            </div>`;
        }
        container.innerHTML = html;
    }
    document.getElementById('profileViewsPanel').classList.add('open');
}

function closeProfileViews() { document.getElementById('profileViewsPanel').classList.remove('open'); }

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
                html += `<div class="grid-item" onclick="openComments('${postId}')">${post.mediaUrl ? (post.mediaType === 'image' ? `<img src="${post.mediaUrl}">` : `<video src="${post.mediaUrl}"></video>`) : '<div class="flex items-center justify-center h-full bg-gray-100 dark:bg-gray-800"><i class="fas fa-file-alt text-2xl text-gray-500"></i></div>'}</div>`;
            }
        }
        container.innerHTML = html || '<div class="text-center p-8 text-gray-500" style="grid-column: span 3;">لا توجد منشورات محفوظة</div>';
    }
    document.getElementById('savedPostsPanel').classList.add('open');
}

function closeSavedPosts() { document.getElementById('savedPostsPanel').classList.remove('open'); }

// ==================== تثبيت المنشور ====================
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

// ==================== إنشاء منشور ====================
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
                        <div><div class="post-username">${escapeHtml(post.userName)}${isUserVerified ? '<i class="fas fa-check-circle verified-badge" style="color: #ec4899; font-size: 14px;"></i>' : ''}</div><div class="post-time">${formatTime(post.timestamp)} ${post.edited ? '· معدل' : ''}</div></div>
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
    if (pinnedId) {
        const pi = postsArray.findIndex(p => p.id === pinnedId);
        if (pi > -1) { const pp = postsArray[pi]; postsArray.splice(pi, 1); postsArray.unshift(pp); }
    }
    allPostsCache = postsArray;
    hasMorePosts = allPostsCache.length > POSTS_PER_PAGE;
    currentDisplayCount = Math.min(POSTS_PER_PAGE, allPostsCache.length);
    const fc = document.getElementById('feedContainer');
    if (fc) { fc.innerHTML = ''; await displayPosts(0, currentDisplayCount); }
}

function resetInfiniteScroll() { isLoadingPosts = false; hasMorePosts = true; allPostsCache = []; currentDisplayCount = 0; }

async function loadFeed() { await loadAllPostsToCache(); }

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
        if (r.type === 'user') html += `<div class="follower-item" onclick="closeSearch(); openProfile('${r.data.uid}')"><div class="post-avatar" style="width: 44px; height: 44px;">${r.data.avatar ? `<img src="${r.data.avatar}">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>'}</div><div><div style="font-weight: 600;">${escapeHtml(r.data.name)}</div><div style="font-size: 12px; color: #8e8e8e;">${escapeHtml(r.data.email)}</div></div></div>`;
        else if (r.type === 'hashtag') html += `<div class="follower-item" onclick="closeSearch(); searchHashtag('${r.data.tag}')"><div class="post-avatar" style="width: 44px; height: 44px; background: linear-gradient(135deg, #ec4899, #f472b6); display: flex; align-items: center; justify-content: center;"><i class="fas fa-hashtag text-white text-xl"></i></div><div><div style="font-weight: 600; color: #ec4899;">#${escapeHtml(r.data.tag)}</div><div style="font-size: 12px; color: #8e8e8e;">${r.data.count} منشور</div></div></div>`;
    }
    document.getElementById('searchResults').innerHTML = html || '<div class="text-center p-4 text-gray-500">لا توجد نتائج</div>';
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
        html += `<div class="chat-message"><div class="message-bubble"><div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;"><span style="font-weight: 600; cursor: pointer;" onclick="closeComments(); openProfile('${comment.userId}')">${escapeHtml(userData?.name || 'مستخدم')}${userData?.verified ? '<i class="fas fa-check-circle" style="color: #ec4899; font-size: 12px;"></i>' : ''}</span><span style="font-size: 10px; color: #8e8e8e;">${formatTime(comment.timestamp)}</span>${comment.id === pinnedId ? '<span style="background: #ec4899; color: white; padding: 2px 6px; border-radius: 12px; font-size: 9px;">📌 مثبت</span>' : ''}</div><div>${escapeHtml(filterBadWords(comment.text))}</div></div></div>`;
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
    document.getElementById('profileName').innerHTML = `${escapeHtml(userData.name)} ${userData.verified ? '<i class="fas fa-check-circle verified-badge" style="color: #ec4899; font-size: 20px;"></i>' : ''}`;
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

// ==================== المحادثات ====================
async function openChat(userId) {
    const s = await db.ref(`users/${userId}`).once('value');
    currentChatUser = s.val();
    document.getElementById('chatUserName').textContent = currentChatUser.name;
    document.getElementById('chatAvatar').innerHTML = currentChatUser.avatar ? `<img src="${currentChatUser.avatar}" style="width:100%;height:100%;object-fit:cover">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>';
    const ls = await db.ref(`users/${userId}/lastSeen`).once('value');
    document.getElementById('chatLastSeen').textContent = ls.val() ? `آخر ظهور ${formatTime(ls.val())}` : '';
    const chatId = getChatId(currentUser.uid, userId);
    listenForTyping(chatId);
    await loadChatMessages(userId);
    document.getElementById('chatPanel').classList.add('open');
}

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
        const lm = Object.values(msgs).sort((a, b) => b.timestamp - a.timestamp)[0];
        convs.push({ userId: oid, userData: us.val(), lastMessage: lm, timestamp: lm.timestamp });
    }
    convs.sort((a, b) => b.timestamp - a.timestamp);
    cl.innerHTML = convs.map(c => `<div class="follower-item" onclick="closeConversations(); openChat('${c.userId}')"><div class="post-avatar" style="width: 48px; height: 48px;">${c.userData?.avatar ? `<img src="${c.userData.avatar}">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>'}</div><div style="flex: 1;"><div style="font-weight: 600;">${escapeHtml(c.userData?.name || 'مستخدم')}</div><div style="font-size: 12px; color: #8e8e8e;">${c.lastMessage.text ? c.lastMessage.text.substring(0, 30) : (c.lastMessage.audioUrl ? 'رسالة صوتية' : 'صورة')}</div></div></div>`).join('');
    document.getElementById('conversationsPanel').classList.add('open');
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

// ==================== لوحة التحكم ====================
async function openAdminPanel() {
    if (currentUser.email !== ADMIN_EMAIL && !currentUser.isAdmin) return showToast('🚫 غير مصرح');
    showToast('💖 جاري تحميل لوحة التحكم...');
    const bws = await db.ref('badWords').once('value');
    const bw = bws.val();
    const bwc = document.getElementById('badWordsList');
    if (bwc) {
        if (!bw) bwc.innerHTML = '<div class="text-center p-4 text-gray-500">لا توجد كلمات ممنوعة</div>';
        else bwc.innerHTML = Object.entries(bw).map(([id, w]) => `<div class="admin-item"><div><span style="font-weight: 600;">🚫 ${escapeHtml(w)}</span></div><button class="admin-delete-btn" onclick="removeBadWord('${id}', '${w}')" style="background: #ef4444; color: white; border: none; padding: 6px 12px; border-radius: 8px; cursor: pointer;">حذف</button></div>`).join('');
    }
    const uss = await db.ref('users').once('value');
    const pss = await db.ref('posts').once('value');
    const css = await db.ref('comments').once('value');
    document.getElementById('adminUsersCount').textContent = uss.exists() ? Object.keys(uss.val()).length : 0;
    document.getElementById('adminPostsCount').textContent = pss.exists() ? Object.keys(pss.val()).length : 0;
    let cc = 0;
    if (css.exists()) for (const pc of Object.values(css.val())) cc += Object.keys(pc).length;
    document.getElementById('adminCommentsCount').textContent = cc;
    
    document.getElementById('adminPanel').classList.add('open');
}

async function verifyUser(userId) { await db.ref(`users/${userId}`).update({ verified: true }); showToast('✅ تم التوثيق'); openAdminPanel(); refreshFeedCache(); }
async function deleteUser(userId) { if (confirm('⚠️ حذف المستخدم؟')) { await db.ref(`users/${userId}`).remove(); showToast('🗑️ تم الحذف'); openAdminPanel(); refreshFeedCache(); } }

function closeAdmin() { document.getElementById('adminPanel').classList.remove('open'); }

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
            html += `<div class="follower-item" onclick="closeFollowers(); openProfile('${uid}')"><div class="post-avatar" style="width: 48px; height: 48px;">${ud?.avatar ? `<img src="${ud.avatar}">` : '<i class="fas fa-user text-white text-xl flex items-center justify-center h-full"></i>'}</div><div><div style="font-weight: 600;">${escapeHtml(ud?.name || 'مستخدم')}</div></div></div>`;
        }
        c.innerHTML = html;
    }
    document.getElementById('followersPanel').classList.add('open');
}
function closeFollowers() { document.getElementById('followersPanel').classList.remove('open'); }

// ==================== دوال الإغلاق ====================
function closeCompose() { document.getElementById('composeModal').classList.remove('open'); document.getElementById('postText').value = ''; document.getElementById('mediaPreview').innerHTML = ''; document.getElementById('mediaPreview').style.display = 'none'; document.getElementById('pollBuilder').style.display = 'none'; document.getElementById('schedulePicker').style.display = 'none'; selectedMediaFile = null; }
function openCompose() { document.getElementById('composeModal').classList.add('open'); }
function closeComments() { document.getElementById('commentsPanel').classList.remove('open'); currentPostId = null; }
function closeProfile() { document.getElementById('profilePanel').classList.remove('open'); }
function closeChat() { document.getElementById('chatPanel').classList.remove('open'); if (isRecording) stopVoiceRecording(); currentChatUser = null; }
function closeConversations() { document.getElementById('conversationsPanel').classList.remove('open'); }
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
"""

# ═══════════════════════════════════════════════════════════
# 💖 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  💖  VIBE 2026 - PREMIUM PINK GLASS EDITION  ✨      ║
║     Ultimate Generator - 5 Files - 3000+ Lines           ║
║                                                          ║
║  ✨  Chat + Video Calls + Stories + Polls             ║
║  🎀  Premium Pink Glass Transparent Design            ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    section("💖 BUILDING FILES - إنشاء الملفات")
    
    write("firebase-config.js", build_config())
    write("auth.html", build_auth())
    write("index.html", build_index())
    write("style.css", build_style())
    write("script.js", build_script())
    
    print(f"""
{'='*60}
  💖 BUILD COMPLETE - تم الإنشاء بنجاح! ✨
{'='*60}

  📊 إحصائيات:
     • {TOTAL_LINES} إجمالي عدد الأسطر
     • 5 ملفات تم إنشاؤها في مجلد {OUTPUT_DIR}/

  📁 الملفات:
     1. firebase-config.js   → إعدادات Firebase + Cloudinary + Agora
     2. auth.html            → تسجيل دخول + اشتراك (Premium Pink)
     3. index.html           → الصفحة الرئيسية + كل الألواح
     4. style.css            → التنسيقات الكاملة (Premium Pink Glass)
     5. script.js            → كل منطق التطبيق (3000+ سطر)

  💖 المميزات الكاملة:
     • 🎀 تصميم زهري فاخر (Premium Pink Glass)
     • 🌙 الوضع الليلي + ⚙️ إعدادات سريعة
     • 📱 Infinite Scroll Feed
     • 💬 محادثات + مؤشر كتابة + رسائل صوتية
     • 📹 مكالمات فيديو (Agora)
     • 📊 استطلاعات رأي + جدولة منشورات
     • 📌 تثبيت + حفظ + اقتباس + مشاركة
     • 🔇 حظر + تقييد + إبلاغ
     • 👁️ تتبع مشاهدات الملف الشخصي
     • 🔍 بحث + هاشتاجات + ترند
     • 🛡️ لوحة تحكم + فلتر كلمات
     • 🎥 مشغل فيديو + 🖼️ عارض صور

  🔑 بيانات الاتصال:
     • Firebase: gomr-3356f
     • Cloudinary: daemk3hut / fok2_k
     • Admin: jasim88v@gmail.com

  💖 للتشغيل: ضع الملفات على سيرفر وافتح auth.html
  💖 VIBE PREMIUM PINK GLASS READY! ✨
{'='*60}
    """)

if __name__ == "__main__":
    main()
