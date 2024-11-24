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

