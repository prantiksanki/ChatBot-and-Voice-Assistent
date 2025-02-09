from prepros import generate_disaster_response
from text2speech import speak_input
from s2t import choose_language, listen, LANGUAGES

def main():
    # Ask the user to choose between chat or talk mode
    mode = input("Choose mode (chat/talk): ").strip().lower()
    
    if mode not in ["chat", "talk"]:
        print("Invalid mode selected. Exiting.")
        return
    
    # Choose language
    lang_code, lang_name = choose_language()
    print(f"Selected Language: {lang_name} ({lang_code})\n")
    
    # Get disaster type
    disaster = input("Enter the type of disaster (e.g., Earthquake, Flood, Fire): ").strip()
    
    # Main loop
    while True:
        print("\nSpeak now...")
        query = listen(lang_code)
        
        if query:
            print(f"User Query: {query}")
            
            # Check for stop keyword
            if "stop" in query.lower():
                print("Stopping the conversation. Goodbye!")
                break
            
            # Generate response
            response = generate_disaster_response(query, disaster)
            
            # Handle response based on mode
            if mode == "chat":
                print(f"Response: {response}\n")
            elif mode == "talk":
                lang_numeric_key = [key for key, value in LANGUAGES.items() if value[0] == lang_code][0]
                speak_input(response, lang_numeric_key)
                print(f"Response: {response}\n")
            

if __name__ == "__main__":
    main()

