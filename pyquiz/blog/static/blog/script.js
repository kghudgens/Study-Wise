'use strict'
// Js for the profile page
function showForm(){
    // Buttons from the profile page
    profileForm.classList.remove('hidden');
    closeBtn.classList.remove('hidden')

    commentFormDiv.classList.remove('hidden')
}

function addHidden(){
    profileForm.classList.add('hidden')
}
// Select the profile div 
const profileForm = document.querySelector('.profile');

// btn that hides form
const closeBtn = document.getElementById('closebtn')
closeBtn.addEventListener('click', addHidden)
console.log(closeBtn)

// Functions that add and removes the hidden class to the form



// Selects the button and store in variable
const updateProfileBtn = document.getElementById('formbtn');

// stored button now using the showform function on any click action
updateProfileBtn.addEventListener('click', showForm);

// Post_Detail js
// Select the comment form div
const commentFormDiv = document.getElementById('comment')
console.log(commentFormDiv);

const commentBtn = document.getElementById('formbtn');
commentBtn.addEventListener('click', showForm)