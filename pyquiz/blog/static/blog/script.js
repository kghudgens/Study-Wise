'strict'
// Js for the profile page
// Select the profile div 
const profileForm = document.querySelector('.profile');

// btn that hides form
const closeBtn = document.getElementById('closebtn')
console.log(closeBtn);

// Functions that add and removes the hidden class to the form
function showForm(){
    profileForm.classList.remove('hidden');
    closeBtn.classList.remove('hidden')
}

function addHidden(){
    profileForm.classList.add('hidden')
}

closeBtn.addEventListener('click', addHidden)

// Selects the button and store in variable
const updateProfileBtn = document.getElementById('formbtn');

// stored button now using the showform function on any click action
updateProfileBtn.addEventListener('click', showForm);

// Post_Detail js