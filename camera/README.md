# ESP32-CAM Streaming Firmware

This folder contains the firmware (`esp32cam_stream.ino`) used to enable live video streaming from the ESP32-CAM module over WiFi.

---

## Requirements

- **Board:** ESP32-CAM (e.g., AI-Thinker module)
- **Development Environment:** Arduino IDE
- **Libraries:** 
  - ESP32 Board Support Package installed in Arduino IDE
  - ESP32 Camera Library (usually included)

---

## Setup Instructions

1. **Install ESP32 Board Manager:**
   - In Arduino IDE, go to `File > Preferences`.
   - Add this URL in "Additional Board Manager URLs":
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
     ```
   - Go to `Tools > Board > Board Manager`, search for "ESP32" and install.

2. **Select Board and Port:**
   - Board: **AI Thinker ESP32-CAM**
   - Port: (Select the correct COM port)

3. **Connect ESP32-CAM to PC:**
   - Use FTDI module (3.3V) or USB-UART converter.
   - Connect `IO0` pin to `GND` during uploading to enable flashing mode.

4. **Upload Firmware:**
   - Open `esp32cam_stream.ino` in Arduino IDE.
   - Replace `YOUR_SSID` and `YOUR_PASSWORD` with your WiFi credentials.
   - Compile and upload.

5. **After Uploading:**
   - Disconnect IO0 from GND.
   - Press the ESP32-CAM Reset Button.
   - Check Serial Monitor (baud rate: 115200) to find IP Address.

6. **Access Stream:**
   - Open a browser and enter the IP Address.
   - The camera feed will be displayed as JPEG images over HTTP.

---

## Important Notes

- Make sure your WiFi router is close enough to the ESP32-CAM for stable connection.
- If streaming is slow, adjust `frame_size` and `jpeg_quality` settings in the code.
- Recommended power supply: At least 5V 1A for ESP32-CAM.

---

