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

    // Reset the form after submission
    form.reset();
  });
});

// Function to save the new anime entry (to be implemented)
function saveEntry(entry) {
  // Implement saving logic here (e.g., to a local file or database)
  console.log("New entry:", entry);
  // You can replace the console.log with actual saving code
}
