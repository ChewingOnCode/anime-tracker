// script.js
import { auth, signInWithEmailAndPassword, signOut } from './firebase.js';
import { displayLoginError, updateLoginUI } from './ui.js';
import { getCurrentUser } from './userAuth.js';

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const logoutButton = document.getElementById('logout-button');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const email = document.getElementById('login-email').value;
        const password = document.getElementById('login-password').value;
        signInWithEmailAndPassword(auth, email, password)
            .then((userCredential) => {
                displayLoginError('Successfully logged in!');
                updateLoginUI(true);
            })
            .catch((error) => {
                displayLoginError('Failed to log in: ' + error.message);
            });
    });

    logoutButton.addEventListener('click', () => {
        signOut(auth).then(() => {
            displayLoginError('Logged out successfully.');
            updateLoginUI(false);
        }).catch((error) => {
            displayLoginError('Error logging out: ' + error.message);
        });
    });

    // Update UI based on auth state
    updateLoginUI(getCurrentUser() != null);
});
