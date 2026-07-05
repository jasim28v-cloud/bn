// 💖 VIBE 2026 - Premium Pink Glass Configuration
// Firebase: gomr-3356f | Cloudinary: daemk3hut
// ✨ PREMIUM: Verified Badges + Chat + Video Calls + Stories

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

// Cloudinary Configuration
const CLOUD_NAME = "daemk3hut";
const UPLOAD_PRESET = "fok2_k";

// Agora Video Call
const AGORA_APP_ID_CALL = "4017f66ea15f4ce088e8d8993a072a5b";

// Admin Account
const ADMIN_EMAIL = 'jasim88v@gmail.com';
const ADMIN_PASSWORD = 'kk2314kk';

// 💖 App Info
const APP_NAME = "VIBE";
const APP_VERSION = "2026.1";
const PRIMARY_COLOR = "#ec4899";
const SECONDARY_COLOR = "#f472b6";

// 💖 Pink Palette
const PINK_COLORS = [
    "linear-gradient(135deg, #ec4899, #f472b6, #fbcfe8)",
    "linear-gradient(135deg, #db2777, #ec4899, #f472b6)",
    "linear-gradient(135deg, #be185d, #db2777, #ec4899)",
    "linear-gradient(135deg, #f472b6, #f9a8d4, #fce7f3)",
    "linear-gradient(135deg, #ec4899, #db2777, #be185d)",
    "linear-gradient(135deg, #831843, #be185d, #ec4899)"
];

console.log('💖 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #ec4899; font-size: 18px; font-weight: bold;');
