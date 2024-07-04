# Cancer-Cell-Detection-from-Images

<p>This project focuses on detecting cancer cells from histopathology images using a deep learning model. It includes a web application that allows users to upload images and get predictions on whether the cells are cancerous or not.</p>

<h2>Table of Contents</h2>
Overview
Directory Structure
Installation
Usage
Model Training
Running the Web Application
Contributing
License

<h2>Overview</h2>
The project uses a convolutional neural network (CNN) to classify histopathology images. It includes data preprocessing, model training, and a web interface to make predictions.

Directory Structure

cancer-cell-detection/
├── app/
│   ├── static/
│   │   └── uploads/             # Directory for uploaded images
│   ├── templates/
│   │   └── upload.html          # HTML template for the web interface
│   ├── __init__.py              # Initialize the Flask app
│   └── routes.py                # Flask routes and logic
├── data/
│   └── breast_histopathology/   # Dataset directory (subdirectories for each class)
├── models/
│   └── cancer_detector.h5       # Trained model file
├── notebooks/
│   └── preprocess_and_train.ipynb # Jupyter notebook for preprocessing and training
├── .gitignore                   # Git ignore file
├── requirements.txt             # Dependencies
└── run.py                       # Script to run the Flask app


1.Installation
Clone the repository:

2.git clone https://github.com/Smrutir798/Cancer-Cell-Detection-from-Images/
cd cancer-cell-detection

3.Install the required packages:
pip install -r requirements.txt


4.Download the dataset:
kaggle datasets download -d paultimothymooney/breast-histopathology-images -p ./data --unzip


5.Usage
 1. Model Training
Run the Jupyter notebook for data preprocessing and model training: jupyter notebook notebooks/preprocess_and_train.ipynb
 2. Ensure the trained model is saved in the models directory as cancer_detector.h5.

6. Running the Web Application
   1. Start the Flask app:
   python run.py
   2. Navigate to http://127.0.0.1:5000 in your web browser to access the web interface and upload images for cancer cell detection.
7. Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
