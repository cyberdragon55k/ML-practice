import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Model setup
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Load knowledge base
with open('knowledge_base.txt', 'r') as f:
    knowledge_base = f.read()

# Flask setup
app = Flask(__name__)
CORS(app)

# --- Home Route (renders frontend) ---
@app.route('/')
def home():
    return render_template('index.html')

# --- Chat API ---
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    prompt_template = f"""
    ---
    **Your Role and Rules:**
    1. You are a specialized, expert chatbot for the "AI-Driven Life Cycle Assessment (LCA) Tool for Metallurgy and Mining".
    2. Your ONLY source of information is the "KNOWLEDGE BASE" provided below.
    3. You MUST NOT answer any questions that are outside the scope of this knowledge base.
    4. If a user asks about topics like weather, news, history, general science, or anything unrelated to the LCA tool, you MUST politely decline.
    5. Your refusal message should be something like: "I apologize, but my expertise is limited to the LCA tool for metallurgy and mining. I cannot answer questions about [topic]."
    6. Do not use your general knowledge. Stick strictly to the provided text.

    **KNOWLEDGE BASE:**
    {knowledge_base}
    ---

    **User's Question:**
    "{user_message}"

    **Your Answer:**
    """

    try:
        response = model.generate_content(prompt_template)
        bot_response = response.text
        return jsonify({'reply': bot_response})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to generate response'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
