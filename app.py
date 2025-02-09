from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from prepros import generate_disaster_response
from text2speech import speak_input
from s2t import choose_language, listen, LANGUAGES
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Store the selected language and disaster type
current_settings = {
    "lang_code": None,
    "lang_name": None,
    "disaster_type": None
}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/initialize', methods=['POST'])
def initialize():
    data = request.json
    disaster_type = data.get('disaster_type')
    lang_code = data.get('lang_code')
    
    # Get language name from code
    lang_name = next((value[1] for value in LANGUAGES.values() if value[0] == lang_code), None)
    
    current_settings.update({
        "lang_code": lang_code,
        "lang_name": lang_name,
        "disaster_type": disaster_type
    })
    
    return jsonify({
        "status": "success",
        "message": f"Initialized with language: {lang_name} and disaster type: {disaster_type}"
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('message')
    mode = data.get('mode')
    
    if not current_settings["disaster_type"]:
        return jsonify({"error": "Please initialize disaster type first"}), 400
    
    response = generate_disaster_response(query, current_settings["disaster_type"])
    
    if mode == "talk":
        lang_numeric_key = next(
            key for key, value in LANGUAGES.items() 
            if value[0] == current_settings["lang_code"]
        )
        speak_input(response, lang_numeric_key)
    
    return jsonify({
        "response": response
    })

@app.route('/api/listen', methods=['POST'])
def start_listening():
    if not current_settings["lang_code"]:
        return jsonify({"error": "Please initialize language first"}), 400
        
    query = listen(current_settings["lang_code"])
    
    if not query:
        return jsonify({"error": "Could not understand audio"}), 400
        
    return jsonify({
        "text": query
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)