document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const title = form.elements["title"].value.trim();
    const synopsis = form.elements["synopsis"].value.trim();
    const genre = form.elements["genre"].value.trim();
    const rating = form.elements["rating"].value.trim();
    const completed = form.elements["completed"].checked;
    const platform = form.elements["platform"].value.trim();

    if (!title || !synopsis || !genre || !rating || !platform) {
      alert("Please fill in all required fields.");
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
    displayEntries();
    form.reset();
  });

  document
    .querySelector("#searchInput")
    .addEventListener("input", displayEntries);
  document
    .querySelector("#genreFilter")
    .addEventListener("change", displayEntries);
  document
    .querySelector("#completedFilter")
    .addEventListener("change", displayEntries);

  function displayEntries() {
    const searchInput = document
      .querySelector("#searchInput")
      .value.toLowerCase();
    const genreFilter = document
      .querySelector("#genreFilter")
      .value.toLowerCase();
    const completedFilter = document.querySelector("#completedFilter").value;

    const entryTable = document.querySelector("#entryTable tbody");
    entryTable.innerHTML = "";

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

        const cellsData = [
          entry.title,
          entry.synopsis,
          entry.genre,
          entry.rating || "N/A",
          entry.completed ? "Yes" : "No",
          entry.platform || "N/A",
        ];
        cellsData.forEach((data) => {
          const cell = row.insertCell();
          cell.textContent = data;
        });

        const editCell = row.insertCell();
        const editButton = document.createElement("button");
        editButton.textContent = "Edit";
        editButton.addEventListener("click", () => {
          editEntry(index);
        });
        editCell.appendChild(editButton);

        const deleteCell = row.insertCell();
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.addEventListener("click", () => {
          deleteEntry;
          displayEntries();
        });
        deleteCell.appendChild(deleteButton);
      }
    });
  }

  function editEntry(index) {
    const entries = getEntries();
    const entry = entries[index];

    const formFields = [
      "title",
      "synopsis",
      "genre",
      "rating",
      "completed",
      "platform",
    ];
    formFields.forEach((field) => {
      const input = document.querySelector(`#${field}`);
      if (input) {
        if (field === "rating") {
          input.value = entry[field] || "";
        } else if (field === "completed") {
          input.checked = entry[field] || false;
        } else {
          input.value = entry[field] || "";
        }
      }
    });

    const entryIndex = document.querySelector("#entryIndex");
    const editBtn = document.querySelector("#editBtn");
    const submitBtn = document.querySelector("#submitBtn");

    if (entryIndex) {
      entryIndex.value = index;
    }
    if (editBtn) {
      editBtn.style.display = "block";
    }
    if (submitBtn) {
      submitBtn.style.display = "none";
    }
  }

  document.querySelector("#editBtn").addEventListener("click", (e) => {
    e.preventDefault();

    const indexElement = document.querySelector("#entryIndex");
    const titleElement = document.querySelector("#title");
    const synopsisElement = document.querySelector("#synopsis");
    const genreElement = document.querySelector("#genre");
    const ratingElement = document.querySelector("#rating");
    const completedElement = document.querySelector("#completed");
    const platformElement = document.querySelector("#platform");

    if (
      titleElement &&
      synopsisElement &&
      genreElement &&
      ratingElement &&
      platformElement
    ) {
      const index = indexElement ? indexElement.value : "";
      const updatedEntry = {
        title: titleElement.value,
        synopsis: synopsisElement.value,
        genre: genreElement.value,
        rating: ratingElement.value,
        completed: completedElement ? completedElement.checked : false,
        platform: platformElement.value,
      };

      updateEntry(index, updatedEntry);
      displayEntries();

      document.querySelector("#animeForm").reset();
      if (indexElement) {
        indexElement.value = "";
      }
      if (completedElement) {
        completedElement.style.display = "none";
      }
      document.querySelector("#editBtn").style.display = "none";
      document.querySelector("#submitBtn").style.display = "block";
    } else {
      console.error(
        "One or more required elements are null. Make sure all elements are present in the document."
      );
    }
  });

  function saveEntry(entry) {
    let entries = JSON.parse(localStorage.getItem("animeEntries")) || [];
    entries.push(entry);
    localStorage.setItem("animeEntries", JSON.stringify(entries));
  }

  function getEntries() {
    return JSON.parse(localStorage.getItem("animeEntries")) || [];
  }

  function deleteEntry(index) {
    let entries = JSON.parse(localStorage.getItem("animeEntries")) || [];
    entries.splice(index, 1); //Remove the entry at the specified index
    localStorage.setItem("animeEntries", JSON.stringify(entries));
  }
  const deleteButton = document.createElement("button");
  deleteButton.textContent = "Delete";
  deleteButton.addEventListener("click", () => {
    deleteEntry(index); // Call deleteEntry function
    displayEntries(); // Refresh entry table after deletion
  });
  deleteCell.appendChild(deleteButton);

  // Function to update an existing anime entry
  function updateEntry(index, updatedEntry) {
    // Get the current list of entries from local storage
    let entries = JSON.parse(localStorage.getItem("animeEntries")) || [];

    // Update the entry at the specified index with the new information
    entries[index] = updatedEntry;

    // Save the updated list back to local storage
    localStorage.setItem("animeEntries", JSON.stringify(entries));
  }

  displayEntries();
});
