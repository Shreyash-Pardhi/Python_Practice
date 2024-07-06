
// Function to show the loading screen
function showLoading() {
    document.querySelector('.loading-overlay').style.display = 'flex';
    document.querySelector('#base-content').classList.add('blurred');
}

// Function to hide the loading screen
function hideLoading() {
    document.querySelector('.loading-overlay').style.display = 'none';
    document.querySelector('#base-content').classList.remove('blurred');
}

// Add event listener to forms and links for showing loading screen
document.addEventListener('DOMContentLoaded', function () {
    // Show loading on form submit
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', showLoading);
    });

    // Show loading on link click
    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function (event) {
            if (link.getAttribute('target') !== '_blank') {
                showLoading();
            }
        });
    });

    // showLoading();
    // window.addEventListener('load', hideLoading);
});
