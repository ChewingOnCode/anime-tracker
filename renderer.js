document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const title = form.elements["title"].value;
    const synopsis = form.elements["synopsis"].value;
    const genre = form.elements["genre"].value;
    const rating = form.elements["rating"].value.trim();
    const completed = form.elements["completed"].checked;
    const platform = form.elements["platform"].value.trim();

    if (!title || !synopsis || !genre || !rating || !platform) {
      alert("Please fill in all required fields."); // Display alert if any required field is empty
      return;
    }
    // Create a new entry object
    const newEntry = {
      title,
      synopsis,
      genre,
      rating,
      completed,
      platform,
      // Add more properties here
    };

    // Call a function to save the new entry (to be implemented)
    saveEntry(newEntry);
    displayEntries(); // Call function to display updated entries
    // Reset the form after submission
    form.reset();
  });
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

      const editCell = row.insertCell(6);
      const editButton = document.createElement("button");
      editButton.textContent = "Edit";
      editButton.addEventListener("click", () => {
        editEntry(index);
      });
      editCell.appendChild(editButton);

      const deleteCell = row.insertCell(7);
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

// Function to edit an existing anime entry
function editEntry(index) {
  const entries = getEntries();
  const entry = entries[index];

  // Fill form fields with entry details for editing
  document.querySelector("#entryIndex").value = index;
  document.querySelector("#title").value = entry.title;
  document.querySelector("#synopsis").value = entry.synopsis;
  document.querySelector("#genre").value = entry.genre;
  document.querySelector("#rating").value = entry.rating || ""; // Use entry.rating if available
  document.querySelector("#completed").checked = entry.completed || false; // Use entry.completed if available
  document.querySelector("#platform").value = entry.platform || ""; // Use entry.platform if available

  // Show the edit button and hide the submit button
  document.querySelector("#editBtn").style.display = "block";
  document.querySelector("#submitBtn").style.display = "none";
}

// Event listener for editing an existing entry
document.querySelector("#editBtn").addEventListener("click", (e) => {
  e.preventDefault();

  const index = document.querySelector("#entryIndex").value;
  const updatedEntry = {
    title: document.querySelector("#title").value,
    synopsis: document.querySelector("#synopsis").value,
    genre: document.querySelector("#genre").value,
    rating: document.querySelector("#rating").value,
    completed: document.querySelector("#completed").checked,
    platform: document.querySelector("#platform").value,
  };

  updateEntry(index, updatedEntry); // Call function to update the entry
  displayEntries(); // Refresh entry table after editing

  // Reset form and hide edit button
  document.querySelector("#animeForm").reset();
  document.querySelector("#entryIndex").value = "";
  document.querySelector("#editBtn").style.display = "none";
  document.querySelector("#submitBtn").style.display = "block";
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

// Function to update an existing anime entry
function updateEntry(index, updatedEntry) {
  const entries = getEntries();
  entries[index] = updatedEntry;
  localStorage.setItem("animeEntries", JSON.stringify(entries));
}
