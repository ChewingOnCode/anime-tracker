// ui.js
function displayAnimes(animeArray, elementId) {
    const animeList = document.getElementById(elementId);
    animeList.innerHTML = '';
    animeArray.forEach(anime => {
        const animeCard = document.createElement('div');
        animeCard.className = 'anime-card';
        animeCard.innerHTML = `<img src="${anime.imgSrc}" alt="${anime.title}" loading="lazy"><h3>${anime.title}</h3>`;
        animeCard.addEventListener('click', () => toggleDetails(anime));
        animeList.appendChild(animeCard);
    });
}

function toggleDetails(anime) {
    const details = document.querySelector('.anime-details') || document.createElement('div');
    if (!details.isConnected) {
        details.className = 'anime-details';
        document.body.appendChild(details);
    }
    const isFavorite = localStorage.getItem(`favorite_${anime.id}`) === 'true';
    details.innerHTML = `<div class="detail-content">
                            <h1>${anime.title}</h1>
                            <p>${anime.description}</p>
                            <button class="toggle-favorite">${isFavorite ? 'Remove Favorite' : 'Add to Favorites'}</button>
                            <button class="close-button">Close</button>
                         </div>`;
    details.style.display = 'block';
    details.querySelector('.toggle-favorite').addEventListener('click', () => toggleFavorite(anime.id));
    details.querySelector('.close-button').addEventListener('click', () => details.style.display = 'none');
}

function toggleFavorite(animeId) {
    const currentStatus = localStorage.getItem(`favorite_${animeId}`) === 'true';
    localStorage.setItem(`favorite_${animeId}`, !currentStatus);
}

document.getElementById('preferences-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const theme = document.getElementById('theme').value;
    const language = document.getElementById('language').value;
    const uid = auth.currentUser.uid; // Make sure the user is logged in
    updateUserData(uid, {
        settings: { theme, language }
    });
});

function updateLoginUI(userIsLoggedIn) {
    const loginFormContainer = document.getElementById('login-form-container');
    const logoutButton = document.getElementById('logout-button');
    if (userIsLoggedIn) {
        logoutButton.style.display = 'block';
        loginFormContainer.style.display = 'none';
    } else {
        logoutButton.style.display = 'none';
        loginFormContainer.style.display = 'block';
    }
}

function displayLoginError(message) {
    const loginError = document.getElementById('login-error');
    loginError.textContent = message;
}

export { displayAnimes, toggleDetails, toggleFavorite, updateLoginUI, displayLoginError };
