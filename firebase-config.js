// ==================== VIBE - Firebase Configuration ====================
const firebaseConfig = {
    apiKey: "AIzaSyDqh0Gtl0lIZl8Rt1PvdE67U8yyhjxpJdw",
    authDomain: "gomr-3356f.firebaseapp.com",
    databaseURL: "https://gomr-3356f-default-rtdb.firebaseio.com",
    projectId: "gomr-3356f",
    storageBucket: "gomr-3356f.firebasestorage.app",
    messagingSenderId: "470296286364",
    appId: "1:470296286364:web:2bb6e28a2095757da88959",
    measurementId: "G-4MLFT3DHJB"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Services
const auth = firebase.auth();
const db = firebase.database();
const storage = firebase.storage();

// Cloudinary
const CLOUD_NAME = 'daemk3hut';
const UPLOAD_PRESET = 'fok2_k';
const AGORA_APP_ID_CALL = '4017f66ea15f4ce088e8d8993a072a5b';

// Admin Account
const ADMIN_EMAIL = 'jasim88v@gmail.com';
const ADMIN_PASSWORD = 'kk2314kk';

// Site Name
const SITE_NAME = 'VIBE';

console.log('✅ VIBE - Firebase, Cloudinary & Agora Ready');
