import speech_recognition as sr

# Language options for Google Speech Recognition
LANGUAGES = {
    "1": ("hi-IN", "हिन्दी"),      # Hindi
    "2": ("bn-IN", "বাংলা"),       # Bengali
    "3": ("te-IN", "తెలుగు"),     # Telugu
    "4": ("gu-IN", "ગુજરાતી"),     # Gujarati
    "5": ("en-US", "English")      # English
}

def choose_language():
    print("Select a language:")
    for key, (_, lang) in LANGUAGES.items():
        print(f"{key}. {lang}")
    
    choice = input("Enter the number of your language: ").strip()
    return LANGUAGES.get(choice, ("hi-IN", "हिन्दी"))  # Default to Hindi if invalid input

def listen(language_code):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio, language=language_code)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

if __name__ == "__main__":
    lang_code, lang_name = choose_language()
    print(f"Listening in {lang_name} ({lang_code})...\n")
    
    while True:
        command = listen(lang_code)
        if command:
            print(command)