# Face Mask Detection Project

This project is a real-time **Face Mask Detection System** that uses transfer learning with the **VGG16 model**. The system can classify images as `with_mask` or `without_mask` and process live webcam feeds for detection.

---

## Features

- **Dataset Splitting**: Automatically organizes images into `with_mask` and `without_mask` folders using the `dataset_create.py` script.
- **Model Training**: Trains a transfer-learned VGG16 model on the COVID-19 face mask dataset using the Jupyter Notebook.
- **Real-Time Detection**: Uses OpenCV to detect and classify mask usage in a live webcam feed.

---

## Prerequisites

Ensure the following are installed on your system:
- Python 3.8 or higher
- Jupyter Notebook
- Required Python libraries (listed in `requirements.txt`)

---

## File Structure

├── dataset_create.py # Script to organize the dataset ├── train_model.ipynb # Jupyter Notebook for training the VGG16 model ├── faceMuskDetection.keras # Trained model (output of the notebook) ├── main.py # Script for real-time mask detection using OpenCV ├── requirements.txt # List of dependencies ├── with_mask/ # Folder for images with masks (generated by dataset_create.py) ├── without_mask/ # Folder for images without masks (generated by dataset_create.py)

yaml
Copy code

---

## How to Use

### Step 1: Prepare the Dataset

1. Place your raw image dataset in a single folder.
2. Run the `dataset_create.py` script to split the images into `with_mask` and `without_mask` folders:
   ```bash
   python dataset_create.py
Step 2: Train the Model
Open the train_model.ipynb file in Jupyter Notebook:
bash
Copy code
jupyter notebook
Follow the instructions in the notebook to train the model using transfer learning on the VGG16 architecture.
After training, the model will be saved as faceMuskDetection.keras.
Step 3: Real-Time Detection
Ensure the trained model (faceMuskDetection.keras) is in the project directory.
Run the main.py script for real-time detection:
bash
Copy code
python main.py
The system will:
Capture frames from your webcam.
Detect and classify with_mask or without_mask in real-time.
Display the result with a color-coded message (Green: Masked, Red: Not Masked).
