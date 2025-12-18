# ⌨️ AI Virtual Keyboard using OpenCV

![Project Demo](https://www.linkedin.com/posts/tejas-tajane-b36451380_computervision-pythondeveloper-handtracking-activity-7407401663617118209-jg9Q?utm_source=share&utm_medium=member_android&rcm=ACoAAF4J0hoBkF3X7g_fyd1UteJGmaGbKVgunp4)
*(Replace the filename above with the actual path to your image if different)*

A fully functional virtual keyboard that allows you to type in mid-air using hand gestures. Built from scratch using **Python**, **OpenCV**, and **MediaPipe**, this project transforms a standard webcam into a touchless input device.

## 🚀 About The Project

This project was born out of a desire to move beyond competitive programming algorithms and build a tangible application using Computer Vision.

The core concept relies on hand-tracking to detect finger positions. By mapping the coordinates of the fingertips to a virtual keyboard layout drawn on the screen, the program detects "clicks" based on the distance between specific fingers. It then simulates real keystrokes using the `pynput` library, allowing you to type into any application (Notepad, Browser, VS Code) using just your camera.

### Key Features
* **Real-time Hand Tracking:** Uses MediaPipe (via cvzone) to track hand landmarks with high precision.
* **Gesture-Based Typing:** "Click" keys by bringing your Index and Middle fingers together.
* **Visual Feedback:** Keys highlight green when clicked to provide user responsiveness.
* **System Integration:** Uses `pynput` to control the actual system keyboard, making it a functional input device, not just a visual demo.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Computer Vision:** OpenCV (`cv2`)
* **Hand Tracking:** cvzone / MediaPipe
* **Input Simulation:** Pynput

## ⚙️ How It Works (The Logic)

1.  **Frame Capture:** The webcam captures video frames which are flipped to create a "mirror" effect for intuitive usage.
2.  **Landmark Detection:** The hand detector identifies 21 landmarks on the hand.
3.  **Coordinate Mapping:** A custom loop draws the keyboard buttons. The program constantly checks if the **Index Finger Tip (Landmark 8)** is within the `(x, y)` coordinates of any button box.
4.  **Click Detection:** To distinguish between "hovering" and "clicking," the program calculates the Euclidean distance between the **Index Finger Tip** and the **Middle Finger Tip**.
    * If the distance drops below a threshold (20 pixels), it registers as a click.
5.  **Output:** The character is drawn to the screen and virtually pressed on the OS level.

## 💻 Installation & Usage

### Prerequisites
Make sure you have Python installed. You can install the required libraries using pip:

```bash
pip install opencv-python cvzone mediapipe pynput
