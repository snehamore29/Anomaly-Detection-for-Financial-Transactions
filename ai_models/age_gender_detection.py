from deepface import DeepFace

def detect_age_gender(image):
    try:
        analysis = DeepFace.analyze(
            image,
            actions=['age', 'gender'],
            enforce_detection=False  # must be False for webcam images
        )
        print("📊 DeepFace analysis:", analysis)
        age = analysis[0]['age']
        gender = analysis[0]['dominant_gender']
        return age, gender
    except Exception as e:
        print("❌ DeepFace error:", str(e))
        return "Unknown", "Unknown"
