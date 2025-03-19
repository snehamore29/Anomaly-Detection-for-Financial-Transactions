import cv2
import numpy as np
import tensorflow as tf

# Load Pre-trained Age/Gender Model (e.g., MobileNet)
model = tf.keras.applications.MobileNetV2(weights='imagenet')

def detect_age_gender(image):
    # Preprocess Image
    image = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image, axis=0)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)

    # Predict Age and Gender
    predictions = model.predict(image)
    age = np.argmax(predictions[0])  # Placeholder for age prediction
    gender = "Male" if predictions[1] > 0.5 else "Female"  # Placeholder for gender prediction
    return age, gender
