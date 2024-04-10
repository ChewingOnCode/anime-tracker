// app.js
const fs = window.tauri.fs;
const filePath = "anime_data.json"; // Use a default file path within your Tauri app

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("animeForm");

  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Get form values
    const animeName = form.elements["animeName"].value.trim();
    const dateWatched = form.elements["dateWatched"].value.trim();
    const rating = parseInt(form.elements["rating"].value, 10);
    const finished = form.elements["finished"].checked;
    const watchedOn = form.elements["watchedOn"].value;
    const language = form.elements["language"].value;

    // Validate form inputs
    if (animeName === "") {
      alert("Please enter the anime name.");
      return;
    }

    if (dateWatched === "") {
      alert("Please select the date watched.");
      return;
    }

    if (isNaN(rating) || rating < 1 || rating > 10) {
      alert("Please enter a valid rating between 1 and 10.");
      return;
    }

    // Create a new row in the UI to display the submitted data
    const table = document.getElementById("animeTable");
    const newRow = table.insertRow(-1);
    newRow.innerHTML = `
      <td>${animeName}</td>
      <td>${dateWatched}</td>
      <td>${rating}</td>
      <td>${finished ? "Yes" : "No"}</td>
      <td>${watchedOn}</td>
      <td>${language}</td>
    `;

    // Reset the form after submission
    form.reset();

    // Write data to file
    const data = {
      animeName,
      dateWatched,
      rating,
      finished,
      watchedOn,
      language,
    };
    writeToFile(data);
  });

  // Sort stored data by date watched
  function sortByDateWatched() {
    const table = document.getElementById("animeTable");
    const rows = Array.from(table.rows).slice(1); // Skip the header row
    rows.sort(
      (a, b) =>
        new Date(a.cells[1].textContent) - new Date(b.cells[1].textContent)
    );
    table.innerHTML = ""; // Clear the table
    table.appendChild(table.rows[0]); // Re-append the header row
    rows.forEach((row) => table.appendChild(row)); // Append sorted rows
  }

  // Filter stored data by finished status
  function filterByFinished() {
    const table = document.getElementById("animeTable");
    const rows = Array.from(table.rows).slice(1); // Skip the header row
    rows.forEach((row) => {
      const finishedCell = row.cells[3];
      const finished = finishedCell.textContent === "Yes";
      row.style.display = finished ? "table-row" : "none";
    });
  }

  // Add event listeners for sorting and filtering
  document
    .getElementById("sortByDateWatched")
    .addEventListener("click", sortByDateWatched);
  document
    .getElementById("filterByFinished")
    .addEventListener("click", filterByFinished);
});

// Function to write data to a file
function writeToFile(data) {
  fs.writeTextFile(filePath, JSON.stringify(data))
    .then(() => {
      console.log("Data written to file successfully.");
    })
    .catch((error) => {
      console.error("Error writing data to file:", error);
    });
}

// Function to read data from a file
function readFromFile() {
  const data = fs.readTextFile(filePath);
  return data ? JSON.parse(data) : [];
}
