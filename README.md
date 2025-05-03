# 🚗 Vehicle Damage Detection

This is a Flask-based web application that allows users to upload images of vehicles and receive predictions about the type of damage detected. The prediction is powered by a pre-trained machine learning model.

---

## 🌟 Features

- Upload vehicle images through a browser interface
- Automatically detect and classify vehicle damage
- Display original and processed image with prediction result

---

## 🗂️ Project Structure

Vehicle-Damage-Detection/
├── app.py # Main Flask application
├── model/
│ └── predict.py # Prediction and preprocessing logic
├── static/
│ └── uploads/ # Uploaded images are saved here
├── templates/
│ └── index.html # HTML template for frontend
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/d1vyadharsh1n1/Vehicle-Damage-Detection.git
cd Vehicle-Damage-Detection
```
### 2. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
```
source venv/bin/activate       # On Windows: venv\Scripts\activate
### 🚀 Run the Application
```bash
python app.py
```
Then open your browser and go to:
http://127.0.0.1:5000/

🧠 How It Works
Users upload an image through the browser.

The app saves the image to the static/uploads/ directory.

The preprocess_and_predict function (in model/predict.py) processes the image and returns:

A prediction label

A path to a visualized output image (if applicable)

The result is displayed on the same page with both original and processed images.


📷 Example (UI)
Select and upload an image of a damaged vehicle.

View the prediction and possibly an annotated version of the image.

Use the output for further analysis or reporting.

🤝 Contributing
Pull requests and suggestions are welcome!
Feel free to fork this repository and submit improvements.

📄 License
This project is licensed under the MIT License.

