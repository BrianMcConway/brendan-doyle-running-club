/* jshint esversion: 8 */
/* global google, bootstrap */

async function initMap() {
    if (!document.getElementById('map')) {
        console.warn("Map element not found, skipping initialization.");
        return;
    }

    const mapElement = document.getElementById('map');
    const fallbackMessage = document.getElementById('map-fallback');

    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    const map = new Map(mapElement, {
        zoom: 10,
        center: { lat: 53.7272, lng: -7.7938 },
        mapId: '26eb5394bc1b80ae'
    });

    const locations = [
        { lat: 53.725090, lng: -7.800639 },
        { lat: 53.669318, lng: -7.985161 },
        { lat: 53.732445, lng: -7.790903 }
    ];

    locations.forEach((location, i) => {
        new AdvancedMarkerElement({
            position: location,
            title: `Location ${i + 1}`,
            map: map
        });
    });

    // Hide the fallback message if the map loads successfully
    if (mapElement) {
        fallbackMessage.style.display = 'none';
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
});
