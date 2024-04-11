// db.js
const sqlite3 = require("sqlite3").verbose();
const db = new sqlite3.Database("anime_database.db");

// Define the database schema
db.serialize(() => {
  db.run(
    "CREATE TABLE IF NOT EXISTS anime_entries (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, synopsis TEXT, genre TEXT, rating TEXT, completed INTEGER, platform TEXT)"
  );
});

// Function to retrieve all anime entries from the database
function getAllEntries(callback) {
  db.all("SELECT * FROM anime_entries", (err, rows) => {
    if (err) {
      console.error(err.message);
    } else {
      callback(rows);
    }
  });
}

// Function to update an existing anime entry
function updateEntry(id, updatedEntry) {
  db.run(
    "UPDATE anime_entries SET title = ?, synopsis = ?, genre = ?, rating = ?, completed = ?, platform = ? WHERE id = ?",
    [
      updatedEntry.title,
      updatedEntry.synopsis,
      updatedEntry.genre,
      updatedEntry.rating,
      updatedEntry.completed,
      updatedEntry.platform,
      id,
    ],
    (err) => {
      if (err) {
        console.error(err.message);
      } else {
        console.log("Anime entry updated successfully.");
      }
    }
  );
}

// Function to delete an anime entry
function deleteEntry(id) {
  db.run("DELETE FROM anime_entries WHERE id = ?", id, (err) => {
    if (err) {
      console.error(err.message);
    } else {
      console.log("Anime entry deleted successfully.");
    }
  });
}

module.exports = { db, saveEntry, getAllEntries, updateEntry, deleteEntry };
