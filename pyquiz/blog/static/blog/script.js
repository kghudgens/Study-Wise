'use strict'

// Select the profile div 
const profileForm = document.querySelector('.profile');

// Select the close button
const closeBtn = document.getElementById('closebtn');

// Selects the button and store in variable
const updateProfileBtn = document.getElementById('formbtn');

// Select the comment form div
const commentFormDiv = document.getElementById('comment')

// Select the comment button for the blog posts
const commentBtn = document.getElementById('formbtn');


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


// btn that hides form

closeBtn.addEventListener('click', addHidden)

// stored button now using the showform function on any click action
updateProfileBtn.addEventListener('click', showForm);

commentBtn.addEventListener('click', showForm)