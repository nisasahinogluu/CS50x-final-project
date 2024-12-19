
# Color Recognition and Upload Application
#### Video Demo:  <https://www.youtube.com/watch?v=YkQQwZKLIf0&t=3s>
## Overview

Welcome to the **Color Recognition and Upload Application**! This web application allows users to upload an image, click on any spot within the image, and instantly view the color of that specific pixel, along with its complementary color. It's designed for anyone interested in exploring color details in images—whether you're a designer, artist, or simply someone curious about colors.

## Features

- **Upload an Image**: Upload any image from your device to the app.
- **Click to Select Color**: Once the image is uploaded, you can click anywhere on the image to select a color.
- **View RGB Value**: The app detects the RGB value of the selected pixel.
- **Complementary Color**: The app calculates and displays the complementary color of the selected color.
- **User-Friendly Interface**: The app is easy to navigate and provides instant feedback.

## How It Works

1. **Upload an Image**: Click on the "Upload Image" button to select an image from your device.
2. **Select a Color**: After uploading the image, simply click on any spot in the image. The app will automatically detect the RGB color value of that spot.
3. **Complementary Color**: The app will then calculate and display the complementary color of the selected color.
4. **Color Information**: Both the selected color and the complementary color will be shown, including color swatches for a more visual representation.

## Technologies Used

- **Flask**: A lightweight Python web framework used to build the backend of the application.
- **HTML/CSS**: For building the frontend user interface.
- **JavaScript**: To handle user interactions and dynamically update the webpage with selected color details.
- **Canvas API**: To extract the color of specific pixels from the uploaded image.

## Installation

To run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/color-recognition-app.git
   cd color-recognition-app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000` to use the app.

## Usage

- Upload an image by selecting a file from your device.
- Click on any point in the uploaded image to see the RGB value and complementary color.
- The color information will be displayed with color boxes for both the selected and complementary colors.

## Contributions

Feel free to fork this repository, submit issues, or create pull requests if you want to contribute. I welcome contributions that improve the functionality, UI/UX, or documentation of the app!


## Contact

- GitHub: https://github.com/nisasahinogluu/CS50x-final-project.git
- LinkedIn: https://www.linkedin.com/in/nisa-şahinoğlu-819a35290/

Enjoy exploring the world of colors!
