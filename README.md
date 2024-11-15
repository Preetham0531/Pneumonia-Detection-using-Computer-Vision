# Pneumonia-Detection-using-Computer-Vision
In this project I implemented a pre-trained VGG-16 model. I trained it with 5200 X-ray Images and achieved an accuracy of 89%. I also created a frontend and backend and hosted a local website.

## **Contents of the Repository**
- **Pneumonia Detection.ipynb**: Jupyter notebook containing code for training and evaluating the pneumonia detection model.
- **Pneumonia detection ppt.pptx**: Presentation explaining the project.
- **app.py**: Flask web application script.
- **model_pneumonia.h5**: Saved trained model file.
- **static/**:
  - `back_ground.jpg`: Background image for the web app.
  - `style.css`: CSS file for styling the web app.
- **templates/**:
  - `index.html`: Homepage of the web application.
  - `result.html`: Page displaying prediction results.
  - `styles.css`: Additional CSS file for further styling.

## **Setup Instructions**
Follow these steps to clone the repository, set up the environment, and run the application.

### Clone the Repository**
```bash
git clone https://github.com/Preetham0531/Pneumonia-Detection-using-Computer-Vision.git
cd Pneumonia-Detection-using-Computer-Vision
```

### Create and Activate Virtual Environment
For Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Run the Application
Start the Flask server by running:
```bash
python app.py
```
The application will be accessible at http://127.0.0.1:5000 in your browser.

