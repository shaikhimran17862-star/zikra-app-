import cv2
import base64
import google.generativeai as genai

# Zikra Camera Module (Only Runs On Command)
def capture_and_analyze(user_command):
    # 1. Check agar user ne photo/camera se juda order diya hai
    trigger_words = ["dekho", "photo", "pic", "camera", "image", "pose"]
    
    if any(word in user_command.lower() for word in trigger_words):
        print("Zikra: Camera open kar rahi hoon...")
        
        # 2. Camera start karke snapshot lena
        cap = cv2.VideoCapture(0)  # Front/Back Camera
        ret, frame = cap.read()
        
        if ret:
            # Image save karke camera instantly CLOSE kar dena (Battery/Privacy Save)
            cv2.imwrite("temp_snapshot.jpg", frame)
            cap.release()
            
            # 3. Gemini Vision API ko image bhejkar opinion lena
            sample_file = genai.upload_file(path="temp_snapshot.jpg")
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            
            prompt = "Aap Zikra ho. Is photo ko dekh kar apni mithi aawaz me ek friendly comment do."
            response = model.generate_content([sample_file, prompt])
            
            return response.text
        else:
            cap.release()
            return "Boss, camera open nahi ho paya. Ek baar permission check kar lijiye."
            
    return None
