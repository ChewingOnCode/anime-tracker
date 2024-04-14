// app.js
import { auth, db, createUserWithEmailAndPassword, signInWithEmailAndPassword, onAuthStateChanged, doc, getDoc, updateDoc, arrayUnion } from './firebase.js';
import { displayAnimes, toggleDetails, toggleFavorite } from './ui.js';

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const sortButton = document.getElementById('sort-button');

    const animes = [
        { id: 1, title: 'Naruto', imgSrc: 'path/to/naruto.jpg', description: 'Description for Naruto' },
        { id: 2, title: 'One Piece', imgSrc: 'path/to/onepiece.jpg', description: 'Description for One Piece' },
        { id: 3, title: 'Attack on Titan', imgSrc: 'path/to/aot.jpg', description: 'Description for Attack on Titan' }
    ];

    displayAnimes(animes, 'anime-list');

    onAuthStateChanged(auth, user => {
        if (user) {
            console.log('User is signed in:', user);
            getDoc(doc(db, 'Users', user.uid))
                .then(docSnapshot => {
                    if (docSnapshot.exists()) {
                        console.log('User data:', docSnapshot.data());
                    } else {
                        console.log('No user data available');
                    }
                });
            updateDoc(doc(db, 'Users', user.uid), {
                lastLogin: new Date().toISOString()
            });
        } else {
            console.log('No user is signed in.');
        }
    });

    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/sw.js').then(registration => {
            console.log('Service Worker registered! Scope:', registration.scope);
        }).catch(err => {
            console.log('Service Worker registration failed:', err);
        });
    }
});
