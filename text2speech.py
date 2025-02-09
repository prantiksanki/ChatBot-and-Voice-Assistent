import gtts
import os
import pygame
import time

def speak_input(input_text, language_code):
    """
    Convert input text to speech in the specified language.
    
    :param input_text: Text to be spoken
    :param language_code: Language code (1-5)
    """
    # Language mapping
    languages = {
        "1": ("hi-IN", "हिन्दी"),      # Hindi
        "2": ("bn-IN", "বাংলা"),       # Bengali
        "3": ("te-IN", "తెలుగు"),     # Telugu
        "4": ("gu-IN", "ગુજરાતી"),     # Gujarati
        "5": ("en-US", "English")      # English
    }
    
    if language_code not in languages:
        raise ValueError("Invalid language code. Choose 1-5.")
    
    lang_code, lang_name = languages[language_code]

    try:
        # Generate speech audio
        audio_file = f"output_{lang_code}.mp3"
        tts = gtts.gTTS(text=input_text, lang=lang_code.split('-')[0])
        tts.save(audio_file)

        # Initialize pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        # Wait until playback finishes
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)

        # Stop and unload the file before deleting
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        time.sleep(0.5)  # Ensure pygame releases the file

        # Remove temporary file
        os.remove(audio_file)

    except Exception as e:
        print(f"Error speaking in {lang_name}: {e}")

    return input_text
