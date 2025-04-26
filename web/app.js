// app.js
// Fetch water level and trash detection data from local server API

const API_URL = "http://192.168.1.100:5000/data"; // Adjust to your Raspberry Pi local server IP and port

async function fetchData() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();

        // Update Water Level
        const waterLevelElement = document.getElementById('water-level');
        waterLevelElement.textContent = data.water_level;
        waterLevelElement.className = `status-box ${data.water_level.toLowerCase()}`;

        // Update Trash Detection
        const trashDetectionElement = document.getElementById('trash-detection');
        trashDetectionElement.textContent = data.trash_detected ? "Trash Detected" : "No Trash Detected";
        trashDetectionElement.className = `status-box ${data.trash_detected ? 'detected' : 'not-detected'}`;

    } catch (error) {
        console.error('Failed to fetch data:', error);
    }
}

// Auto-refresh every 5 seconds
setInterval(fetchData, 5000);

// Initial fetch
fetchData();
