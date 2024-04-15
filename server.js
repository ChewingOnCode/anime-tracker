const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

// Serve static files from 'public' directory
app.use(express.static('public'));
app.use(express.json());

// Additional route to ensure the root path serves the index.html file
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Configure Multer for file uploads
const storage = multer.diskStorage({
    destination: function(req, file, cb) {
        cb(null, 'uploads/')  // ensure this directory exists
    },
    filename: function(req, file, cb) {
        cb(null, file.fieldname + '-' + Date.now() + path.extname(file.originalname))
    }
});

const upload = multer({ storage: storage });

// Endpoint to handle form submissions
app.post('/addAnime', upload.single('coverImage'), (req, res) => {
    const animeData = {
        title: req.body.title,
        dateWatched: req.body.dateWatched,
        rating: req.body.rating,
        language: req.body.language,
        coverImage: req.file ? req.file.path : 'No Image Uploaded'
    };

    // Update anime list JSON file
    fs.readFile('anime-list.json', (err, data) => {
        if (err) {
            console.error('Error reading file:', err);
            return res.status(500).send('Error reading data file');
        }

        let animeList = JSON.parse(data);
        animeList.push(animeData);

        fs.writeFile('anime-list.json', JSON.stringify(animeList, null, 4), (err) => {
            if (err) {
                console.error('Error writing file:', err);
                return res.status(500).send('Error updating data file');
            }
            res.send('Anime added successfully');
        });
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
