// userAuth.js
import { auth, onAuthStateChanged } from './firebase.js';

let currentUser = null;

onAuthStateChanged(auth, user => {
    currentUser = user;
    if (user) {
        console.log('User is signed in:', user);
    } else {
        console.log('No user is signed in.');
    }
});

function getCurrentUser() {
    return currentUser;
}

export { getCurrentUser };
