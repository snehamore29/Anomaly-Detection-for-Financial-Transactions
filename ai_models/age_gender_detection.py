from deepface import DeepFace

def detect_age_gender(image):
    # Analyze the image for age and gender
    analysis = DeepFace.analyze(image, actions=['age', 'gender'], enforce_detection=False)
    age = analysis[0]['age']
    gender = analysis[0]['dominant_gender']
    return age, gender
