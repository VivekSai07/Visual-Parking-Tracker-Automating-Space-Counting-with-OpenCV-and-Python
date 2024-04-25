# Visual Parking Tracker Automating Space Counting with OpenCV and Python
This project utilizes OpenCV to detect car parking spaces in a given video feed. It analyzes each frame to determine the occupancy of parking spots, marking them accordingly. The program provides real-time feedback on the number of free parking spaces available.

## Features

- Detects parking spaces in a video feed.
- Calculates the number of free parking spots in real-time.
- Utilizes OpenCV for image processing and analysis.

## Parking Space Selector

This [ParkingSpacePicker.py](https://github.com/VivekSai07/Visual-Parking-Tracker-Automating-Space-Counting-with-OpenCV-and-Python/blob/main/ParkingSpacePicker.py) script allows users to manually select and mark car parking spaces on an image. It provides a simple interface where users can click to mark parking spots and undo markings if necessary. The positions of the parking spaces are saved using pickle, allowing for easy retrieval and modification.

## Usage
1. Clone the repository:
```bash
git clone https://github.com/VivekSai07/Visual-Parking-Tracker-Automating-Space-Counting-with-OpenCV-and-Python.git
```
2. Run the script:
```bash
python parking_space_selector.py
```
3. Click on the image to mark parking spaces.
4. Right-click on a marked space to undo the marking.
5. Press 'q' to exit the program.
6. Use/Replace carPark.mp4 with your desired video file.
7. Run the script:
```bash
python car_parking_detector.py
```
8. Press 'q' to exit the program.
