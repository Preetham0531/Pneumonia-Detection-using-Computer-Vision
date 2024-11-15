from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model('model_pneumonia.h5')  # Load your model

def preprocess_image(img_path):
    # Resize the image to 150x150 (as expected by your model)
    img = image.load_img(img_path, target_size=(150, 150))  # Adjust to (150, 150)
    img = image.img_to_array(img) / 255.0  # Normalize if needed
    img = np.expand_dims(img, axis=0)      # Add batch dimension
    return img

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            # Ensure the uploads folder exists
            uploads_dir = os.path.join('static', 'uploads')
            if not os.path.exists(uploads_dir):
                os.makedirs(uploads_dir)  # Create the directory if it doesn't exist
            
            # Save the file
            file_path = os.path.join(uploads_dir, file.filename)
            file.save(file_path)
            img = preprocess_image(file_path)
            prediction = model.predict(img)
            label = "Normal" if prediction[0][0] > 0.5 else "Pneumonia Detected"
            return render_template("result.html", label=label, file_path=file_path)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
