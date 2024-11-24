import cv2
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('faceMuskDetection.keras')

cap = cv2.VideoCapture(0)




def detect_musk(img):
   
    img_resized = cv2.resize(img, (224, 224))
    img_resized = img_resized.reshape(1, 224, 224, 3)  # Add batch dimension
    img_resized = img_resized / 255.0  # Normalize the image to [0, 1]
    y_pred = model.predict(img_resized)  # Get probabilities
    
 
    if len(y_pred.shape) == 2 and y_pred.shape[1] > 1:
        predicted_class = np.argmax(y_pred, axis=1)[0]  
    else:
        print(y_pred[0][0])
        predicted_class = int(y_pred[0][0] > 0.8)  #thresold 0.8
    
    return predicted_class


while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame from webcam.")
        break


    y_pred = detect_musk(frame)

   
    label = "Musked" if y_pred == 0 else "No Musked"
    color = (0, 255, 0) if y_pred == 0 else (0, 0, 255)  # Green for "Musked", Red for "No Musked"


    cv2.putText(
        frame, label, (50, 50), 
        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA
    )

   
    cv2.imshow('Musk Detection', frame)

    # Break the loop if 'x' is pressed
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
