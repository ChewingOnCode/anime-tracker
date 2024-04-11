document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const title = form.elements["title"].value.trim(); // Trim whitespace
    const synopsis = form.elements["synopsis"].value.trim();
    const genre = form.elements["genre"].value.trim();
    const rating = form.elements["rating"].value.trim();
    const completed = form.elements["completed"].checked;
    const platform = form.elements["platform"].value.trim();

    if (!title || !synopsis || !genre || !rating || !platform) {
      alert("Please fill in all required fields."); // Display alert if any required field is empty
      return;
    }

    const newEntry = {
      title,
      synopsis,
      genre,
      rating,
      completed,
      platform,
    };

    saveEntry(newEntry);
    displayEntries(); // Call function to display updated entries
    form.reset(); // Reset the form after submission
  });

  document.querySelector("#searchInput").addEventListener("input", () => {
    displayEntries(); // Call displayEntries() on input change to update the displayed entries
  });

  document.querySelector("#genreFilter").addEventListener("change", () => {
    displayEntries(); // Call displayEntries() on filter change to update the displayed entries
  });

  document.querySelector("#completedFilter").addEventListener("change", () => {
    displayEntries(); // Call displayEntries() on filter change to update the displayed entries
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
  // Function to display all anime entries with search and filter functionality
  function displayEntries() {
    const searchInput = document
      .querySelector("#searchInput")
      .value.toLowerCase();
    const genreFilter = document
      .querySelector("#genreFilter")
      .value.toLowerCase();
    const completedFilter = document.querySelector("#completedFilter").value;

    console.log("Search Input:", searchInput);
    console.log("Genre Filter:", genreFilter);
    console.log("Completed Filter:", completedFilter);

    const entryTable = document.querySelector("#entryTable tbody");
    entryTable.innerHTML = ""; // Clear existing table body

    const entries = getEntries();

    entries.forEach((entry, index) => {
      if (
        (searchInput === "" ||
          entry.title.toLowerCase().includes(searchInput)) &&
        (genreFilter === "" || entry.genre.toLowerCase() === genreFilter) &&
        (completedFilter === "" ||
          (completedFilter === "yes" && entry.completed) ||
          (completedFilter === "no" && !entry.completed))
      ) {
        const row = entryTable.insertRow();

        const titleCell = row.insertCell(0);
        titleCell.textContent = entry.title;

        const synopsisCell = row.insertCell(1);
        synopsisCell.textContent = entry.synopsis;

        const genreCell = row.insertCell(2);
        genreCell.textContent = entry.genre;

        const ratingCell = row.insertCell(3);
        ratingCell.textContent = entry.rating || "N/A";

        const completionCell = row.insertCell(4);
        completionCell.textContent = entry.completed ? "Yes" : "No";

        const platformCell = row.insertCell(5);
        platformCell.textContent = entry.platform || "N/A";

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
      }
    });
  }
  // Function to delete an anime entry from local storage
  function deleteEntry(index) {
    let entries = JSON.parse(localStorage.getItem("animeEntries")) || [];
    entries.splice(index, 1);
    localStorage.setItem("animeEntries", JSON.stringify(entries));
  }
  displayEntries(); // Initial display of entries when the app loads
});
