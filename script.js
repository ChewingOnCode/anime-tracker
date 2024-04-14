import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js';
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, onAuthStateChanged } from 'https://www.gstatic.com/firebasejs/9.0.0/firebase-auth.js';

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
  

function signUpWithEmailPassword(email, password) {
    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            console.log('User created and signed in:', userCredential.user);
        })
        .catch((error) => {
            console.error('Error signing up:', error.message);
        });
}

function signInWithEmailPassword(email, password) {
    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            console.log('User signed in:', userCredential.user);
        })
        .catch((error) => {
            console.error('Error signing in:', error.message);
        });
}
// script.js
document.addEventListener('DOMContentLoaded', () => {
    const animeList = document.getElementById('anime-list');
    const searchInput = document.getElementById('search-input');
    const sortButton = document.getElementById('sort-button');

    // Sample data with description included
    const animes = [
        { id: 1, title: 'Naruto', imgSrc: 'path/to/naruto.jpg', description: 'Description for Naruto' },
        { id: 2, title: 'One Piece', imgSrc: 'path/to/onepiece.jpg', description: 'Description for One Piece' },
        { id: 3, title: 'Attack on Titan', imgSrc: 'path/to/aot.jpg', description: 'Description for Attack on Titan' }
    ];

    const genres = {
        'Naruto': ['Action', 'Adventure'],
        'One Piece': ['Adventure', 'Fantasy'],
        'Attack on Titan': ['Action', 'Drama']
    };

    function displayAnimes(animeArray) {
        animeList.innerHTML = '';
        animeArray.forEach(anime => {
            const animeCard = document.createElement('div');
            animeCard.className = 'anime-card';
            animeCard.innerHTML = `<img src="${anime.imgSrc}" alt="${anime.title}" loading="lazy"><h3>${anime.title}</h3>`;
            animeCard.addEventListener('click', () => toggleDetails(anime));
            animeList.appendChild(animeCard);
        });
    }

    function filterAnimesByGenre(genre) {
        const filteredAnimes = animes.filter(anime => genres[anime.title].includes(genre));
        displayAnimes(filteredAnimes);
    }
    
    function toggleDetails(anime) {
        let details = document.querySelector('.anime-details');
        if (!details) {
            details = document.createElement('div');
            details.className = 'anime-details';
            document.body.appendChild(details);
        }

        const isFavorite = localStorage.getItem(`favorite_${anime.id}`) === 'true';
        details.innerHTML = `
            <div class="detail-content">
                <h1>${anime.title}</h1>
                <p>${anime.description}</p>
                <button class="toggle-favorite">${isFavorite ? 'Remove Favorite' : 'Add to Favorites'}</button>
                <button class="close-button">Close</button>
            </div>`;
        details.style.display = 'block';

        details.querySelector('.toggle-favorite').addEventListener('click', () => toggleFavorite(anime.id));
        details.querySelector('.close-button').addEventListener('click', () => {
            details.style.display = 'none';
        });
    }

    function toggleFavorite(animeId) {
        const currentStatus = localStorage.getItem(`favorite_${animeId}`) === 'true';
        localStorage.setItem(`favorite_${animeId}`, !currentStatus);
        const anime = animes.find(anime => anime.id === animeId);
        toggleDetails(anime); // Refresh the details view to update the button text
    }

    searchInput.oninput = () => {
        const searchText = searchInput.value.toLowerCase();
        const filteredAnimes = animes.filter(anime => anime.title.toLowerCase().includes(searchText));
        displayAnimes(filteredAnimes);
    };


if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
        .then(registration => {
            console.log('Service Worker registered! Scope:', registration.scope);
        })
        .catch(err => {
            console.log('Service Worker registration failed:', err);
        });
    });
}
    displayAnimes(animes);  // Initial display
});