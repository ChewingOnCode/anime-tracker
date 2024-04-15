// Modal controls
const modal = document.getElementById('addAnimeModal');
const btn = document.getElementById('addAnimeBtn'); // The button that opens the modal
const span = document.getElementsByClassName('close-button')[0]; // The "x" element that closes the modal
const detailsModal = document.getElementById('detailsModal'); // Details modal
let animeList = []; // Assuming animeList is stored or fetched initially

// Modal display controls
btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal || event.target == detailsModal) {
        modal.style.display = "none";
        detailsModal.style.display = "none";
    }
}

// Fetch data and display it
function fetchData() {
    fetch('anime-list.json')
        .then(response => response.json())
        .then(data => {
            animeList = data; // Store fetched data in global variable
            displayData(data);
        })
        .catch(error => console.error('Failed to fetch data:', error));
}

// Display anime data in the UI
function displayData(animeList) {
    const container = document.getElementById('anime-container');
    container.innerHTML = '';  // Clear existing content
    animeList.forEach(anime => {
        const card = document.createElement('div');
        card.className = 'anime-card';
        const image = document.createElement('img');
        image.src = anime.coverImage; // Assuming each anime has a coverImage field
        image.onclick = function() {
            showDetailsModal(anime);
        };
        const title = document.createElement('h3');
        title.textContent = anime.title;
        card.appendChild(title);
        card.appendChild(image);
        container.appendChild(card);
    });
}

// Show detailed information in a modal
function showDetailsModal(anime) {
    detailsModal.innerHTML = `
        <h3>${anime.Title}</h3>
        <p>Episode: ${anime["Episode Number"]}</p>
        <p>Seasons: ${anime.Seasons}</p>
        <p>Release Date: ${anime["Release Date"]}</p>
        <p>Watched on: ${anime["Last Watched"]}</p>
        <p>Rating: ${anime.Rating}/10</p>
        <p>Genre: ${anime.Genre}</p>
        <p>Sub-Genre: ${anime["Sub-Genre"]}</p>
        <p>Cliffhanger: ${anime["Ends on a Cliffhanger"]}</p>
        <p>Themes: ${anime.Themes}</p>
    `;
    detailsModal.style.display = "block";
}

// Add new anime entry from form submission
function addNewAnime(event) {
    event.preventDefault();  // Prevent form submission from reloading the page
    const formData = new FormData(document.getElementById('animeForm'));
    
    fetch('/addAnime', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())  // Assuming the server responds with JSON
    .then(data => {
        displayData(data);  // Assuming server returns the updated list
        modal.style.display = "none"; // Hide the form modal after submission
    })
    .catch(error => console.error('Error:', error));
}


// Event listeners
document.addEventListener('DOMContentLoaded', fetchData);
document.getElementById('animeForm').addEventListener('submit', addNewAnime);
