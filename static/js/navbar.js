const menuIcon = document.querySelector('.menuIcon');
const hidden_when_mobile_Active = document.querySelector('.hidden_when_mobile_Active');

menuIcon.addEventListener('click', function () {
    hidden_when_mobile_Active.classList.toggle('showMenu');
});


const profile = document.querySelector('.profile');
const profileButton = document.querySelector('.image_and_name');

if (profile) {

    profileButton.addEventListener('click', function () {

        if (window.innerWidth <= 768) {
            profile.classList.toggle('active');
        }

    });

}