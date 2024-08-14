async function initMap() {
    if (!document.getElementById('map')) {
        console.warn("Map element not found, skipping initialization.");
        return;
    }

    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    const map = new Map(document.getElementById('map'), {
        zoom: 10,
        center: { lat: 53.7272, lng: -7.7938 }, // Centered over Longford, Ireland
        mapId: '26eb5394bc1b80ae' // Replace with your actual map ID
    });

    const locations = [
        { lat: 53.725090, lng: -7.800639 }, // Harbour Row location
        { lat: 53.669318, lng: -7.985161 }, // Lanesboro Track location
        { lat: 53.732445, lng: -7.790903 }  // Mall Complex location
    ];

    locations.forEach((location, i) => {
        new AdvancedMarkerElement({
            position: location,
            title: `Location ${i + 1}`,
            map: map
        });
    });

    // Check if the map is visible and toggle the fallback message
    const fallbackMessage = document.getElementById('map-fallback');

    if (fallbackMessage) {
        const mapElement = document.getElementById('map');
        if (mapElement && mapElement.innerHTML.trim() === '') {
            fallbackMessage.style.display = 'block';
        } else {
            fallbackMessage.style.display = 'none';
        }
    }
}

window.initMap = initMap;

document.addEventListener('DOMContentLoaded', function () {
    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
    toastElList.forEach(function (toastEl) {
        var toast = new bootstrap.Toast(toastEl, {
            delay: 3000 // 3 seconds
        });
        toast.show();
    });

    // Ensure the script checks the map visibility on page load
    const mapElement = document.getElementById('map');
    const fallbackMessage = document.getElementById('map-fallback');

    if (fallbackMessage) {
        if (mapElement && mapElement.innerHTML.trim() === '') {
            fallbackMessage.style.display = 'block';
        } else {
            fallbackMessage.style.display = 'none';
        }
    }
});
