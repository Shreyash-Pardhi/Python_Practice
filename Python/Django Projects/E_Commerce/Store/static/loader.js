// loader.js
document.addEventListener("DOMContentLoaded", function() {
    var loader = document.getElementById('wheel-and-hamster');
    var body = document.getElementById('ad')

    function showLoader() {
        loader.style.display = 'normal';
        body.style.display = 'none'; // Hide content
    }

    function hideLoader() {
        loader.style.display = 'none';
        body.style.display = 'block'; // Show content
    }

    // Show loader on link click
    document.querySelectorAll('a').forEach(function(link) {
        link.addEventListener('click', function(event) {
            if (link.getAttribute('href') !== '#') {
                showLoader();
            }
        });
    });

    // Show loader on form submit
    document.querySelectorAll('form').forEach(function(form) {
        form.addEventListener('submit', function(event) {
            showLoader();
        });
    });

    // Hide loader when the page is fully loaded
    window.addEventListener('load', function() {
        hideLoader();
    });

    // Initially show the loader and hide the body content
    showLoader();
});
