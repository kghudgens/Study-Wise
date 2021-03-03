'strict'
// Select the profile div 
const profileForm = document.querySelector('.profile');

// Function that removes the display style to the form
function showForm(){
    profileForm.classList.remove('hidden');
    // BUG
    const closeBtn = document.querySelector('.closebtn')
    closeBtn.addEventListener('click', function(){
        profileForm.classList.add('.hidden')
        }
    )
}

// Selects the button and store in variable
const updateProfileBtn = document.getElementById('formbtn');

// stored button now using the showform function on any click action
updateProfileBtn.addEventListener('click', showForm);