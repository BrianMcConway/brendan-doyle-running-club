async function initMap() {
    try {
        const { Map } = await google.maps.importLibrary("maps");
        const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

        const map = new Map(document.getElementById('map'), {
            zoom: 10,
            center: { lat: 53.7272, lng: -7.7938 }, // Centered over Longford, Ireland
            mapId: 'DEMO_MAP_ID' // Replace with your actual map ID
        });

        const locations = [
            { lat: 53.725090, lng: -7.800639 }, // Harbour Row location
            { lat: 53.669318, lng: -7.985161 }, // Lanesboro Track location
            { lat: 53.732445, lng: -7.790903 }  // Mall Complex location
        ];

        locations.forEach((location, i) => {
            new AdvancedMarkerElement({
                map: map,
                position: location,
                title: `Location ${i + 1}`
            });
        });
    } catch (error) {
        console.error("Failed to initialize map: ", error);
    }
}

window.initMap = initMap;

