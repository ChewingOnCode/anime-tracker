// app.js
const fs = window.tauri.fs;
// Function to write data to a file
function writeToFile(data) {
    fs.writeTextFile('anime_data.json', JSON.stringify(data));
}

// Function to read data from a file
function readFromFile() {
    const data = fs.readTextFile('anime_data.json');
    return data ? JSON.parse(data) : [];
}
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('animeForm');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Get form values
        const animeName = form.elements['animeName'].value;
        const dateWatched = form.elements['dateWatched'].value;
        const rating = form.elements['rating'].value;
        const finished = form.elements['finished'].checked;
        const watchedOn = form.elements['watchedOn'].value;
        const language = form.elements['language'].value;

        // Create a new row in the UI to display the submitted data
        const table = document.getElementById('animeTable');
        const newRow = table.insertRow(-1);
        newRow.innerHTML = `
            <td>${animeName}</td>
            <td>${dateWatched}</td>
            <td>${rating}</td>
            <td>${finished ? 'Yes' : 'No'}</td>
            <td>${watchedOn}</td>
            <td>${language}</td>
        `;

        // Reset the form after submission
        form.reset();
    });
});

// Sort stored data by date watched
function sortByDateWatched() {
    const storedData = readFromFile();
    if (storedData) {
        storedData.sort((a, b) => new Date(a.dateWatched) - new Date(b.dateWatched));
        displayAnimeData(storedData); // Update the UI with sorted data
    }
}

// Filter stored data by finished status
function filterByFinished() {
    const storedData = readFromFile();
    const filteredData = storedData.filter(data => data.finished);
    displayFilteredData(filteredData); // Update the UI with filtered data
}