document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const title = form.elements["title"].value;
    const synopsis = form.elements["synopsis"].value;
    const genre = form.elements["genre"].value;
    // Add more fields as needed

    // Create a new entry object
    const newEntry = {
      title,
      synopsis,
      genre,
      // Add more properties here
    };

    // Call a function to save the new entry (to be implemented)
    saveEntry(newEntry);
    displayEntries(); // Call function to display updated entries
    // Reset the form after submission
    form.reset();
  });
  // Function to display all anime entries
  // Function to display all anime entries in a table format
  function displayEntries() {
    const entryTable = document.querySelector("#entryTable tbody");
    entryTable.innerHTML = ""; // Clear existing table body

    const entries = getEntries();

    entries.forEach((entry, index) => {
      const row = entryTable.insertRow();

      const titleCell = row.insertCell(0);
      titleCell.textContent = entry.title;

      const synopsisCell = row.insertCell(1);
      synopsisCell.textContent = entry.synopsis;

      const genreCell = row.insertCell(2);
      genreCell.textContent = entry.genre;

      const ratingCell = row.insertCell(3);
      ratingCell.textContent = entry.rating || "N/A"; // Use entry.rating if available, otherwise 'N/A'

      const completionCell = row.insertCell(4);
      completionCell.textContent = entry.completed ? "Yes" : "No";

      const platformCell = row.insertCell(5);
      platformCell.textContent = entry.platform || "N/A"; // Use entry.platform if available, otherwise 'N/A'

      const deleteCell = row.insertCell(6);
      const deleteButton = document.createElement("button");
      deleteButton.textContent = "Delete";
      deleteButton.addEventListener("click", () => {
        deleteEntry(index);
        displayEntries(); // Refresh entry table after deletion
      });
      deleteCell.appendChild(deleteButton);
    });
  }
  // Initial display of entries when the app loads
  displayEntries();
});

// Function to save the new anime entry to local storage
function saveEntry(entry) {
  let entries = JSON.parse(localStorage.getItem("animeEntries")) || [];
  entries.push(entry);
  localStorage.setItem("animeEntries", JSON.stringify(entries));
}

// Function to get all anime entries from local storage
function getEntries() {
  return JSON.parse(localStorage.getItem("animeEntries")) || [];
}

// Function to delete an anime entry from local storage
function deleteEntry(index) {
  let entries = JSON.parse(localStorage.getItem("animeEntries")) || [];
  entries.splice(index, 1);
  localStorage.setItem("animeEntries", JSON.stringify(entries));
}
