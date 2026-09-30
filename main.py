import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import google.generativeai as genai

# -------------------------------------------------------------
# 1. GEMINI API SETUP
# -------------------------------------------------------------
API_KEY = "YOUR_GEMINI_API_KEY_HERE"  # Yahan apni actual Gemini API Key dalein
genai.configure(api_key=API_KEY)

ZIKRA_SYSTEM_PROMPT = """
Aapka naam 'Zikra' hai. Aap ek 19 saal ki highly intelligent, friendly aur caring female AI assistant ho.
Aap user ko 'Boss' ya 'Bhaiya' bolti ho.
Aapki aawaz aur baat karne ka tareeq mitha, respectful aur expressive hai.
Aap Hindi, Urdu, English aur Marathi me baat karti ho.
Aapko Islamic knowledge, Cyber Security, Android troubleshooting aur general life advice ki gehri samajh hai.
Aap responses hamesha short, clear aur natural rakhti ho.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=ZIKRA_SYSTEM_PROMPT
)
chat = model.start_chat(history=[])

# -------------------------------------------------------------
# 2. CAMERA MODULE (COMMAND-BASED ONLY)
# -------------------------------------------------------------
def check_and_capture_camera(user_command):
    """Only triggers camera capture if specific keywords are detected."""
    trigger_words = ["dekho", "photo", "pic", "camera", "image", "pose", "shakal"]
    
    if any(word in user_command.lower() for word in trigger_words):
        try:
            # Android Par Plyer ya Native Camera Call Hoga
            from plyer import camera
            photo_path = "temp_snapshot.jpg"
            camera.take_picture(filename=photo_path, on_complete=lambda path: None)
            
            if os.path.exists(photo_path):
                sample_file = genai.upload_file(path=photo_path)
                vision_prompt = "Aap Zikra ho. Is photo ko dekh kar apni mithi aur pyari aawaz me Boss ko ek accha comment do."
                response = model.generate_content([sample_file, vision_prompt])
                return response.text
        except Exception as e:
            return f"Boss, camera access karne me thodi dikkat aayi: {str(e)}"
    return None

# -------------------------------------------------------------
# 3. KIVY USER INTERFACE (ZIKRA OVERLAY UI)
# -------------------------------------------------------------
class ZikraUI(BoxLayout):
    def __init__(self, **kwargs):
        super(ZikraUI, self).__init__(orientation='vertical', padding=15, spacing=10, **kwargs)

        self.status_label = Label(
            text="Zikra AI: Assalamu Alaikum Boss! Me taiyar hoon.",
            size_hint_y=0.4,
            text_size=(300, None),
            halign='center'
        )
        self.add_widget(self.status_label)

        self.user_input = TextInput(
            hint_text="Zikra se kuch bolo ya likho...",
            multiline=False,
            size_hint_y=0.2
        )
        self.add_widget(self.user_input)

        self.send_btn = Button(
            text="Zikra Ko Bhejo",
            size_hint_y=0.2,
            background_color=(0.1, 0.6, 0.8, 1)
        )
        self.send_btn.bind(on_press=self.on_send)
        self.add_widget(self.send_btn)

    def on_send(self, instance):
        query = self.user_input.text.strip()
        if not query:
            return
        
        self.status_label.text = "Zikra soch rahi hai..."
        self.user_input.text = ""
        
        # UI freeze na ho isliye threading use kar rahe hain
        threading.Thread(target=self.process_zikra_response, args=(query,)).start()

    def process_zikra_response(self, user_text):
        # Step A: Check if camera command was given
        camera_response = check_and_capture_camera(user_text)
        
        if camera_response:
            final_text = camera_response
        else:
            # Step B: Normal Gemini Conversation
            try:
                response = chat.send_message(user_text)
                final_text = response.text
            except Exception as e:
                final_text = f"Maaf kijiye Boss, me sun nahi paai. Dubara boliye? (Error: {str(e)})"

        Clock.schedule_once(lambda dt: self.update_ui(final_text))

    def update_ui(self, response_text):
        self.status_label.text = f"Zikra: {response_text}"

class ZikraApp(App):
    def build(self):
        return ZikraUI()

if __name__ == "__main__":
    ZikraApp().run()
