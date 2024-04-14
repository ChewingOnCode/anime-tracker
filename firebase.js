import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js';
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, onAuthStateChanged } from 'https://www.gstatic.com/firebasejs/9.0.0/firebase-auth.js';
import { getFirestore, doc, getDoc, setDoc, updateDoc, arrayUnion } from 'https://www.gstatic.com/firebasejs/9.0.0/firebase-firestore.js';

const firebaseConfig = {

    apiKey: "AIzaSyDBDgTSFe6X1yQUd9UyU9Js8K6b5xmu3ps",

    authDomain: "anime-series-tracker.firebaseapp.com",

    projectId: "anime-series-tracker",

    storageBucket: "anime-series-tracker.appspot.com",

    messagingSenderId: "629251925289",

    appId: "1:629251925289:web:631285d0ba2c0efd79c338"

  };
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);  

export { auth, db, createUserWithEmailAndPassword, signInWithEmailAndPassword, onAuthStateChanged, doc, getDoc, setDoc, updateDoc, arrayUnion };