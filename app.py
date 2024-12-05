from flask import Flask, request, render_template, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)

# Allow CORS for GitHub Pages URL and YouTube domain
CORS(app, origins=["https://yourfrontend.github.io", "https://www.youtube.com"])

# Set your OpenAI API key securely (avoid hardcoding in production)
openai.api_key = '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'  # Replace with your actual OpenAI API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        question = request.json.get('question')  # Get the question from JSON
        if not question:
            return jsonify({'error': 'No question provided'}), 400  # Return error if no question

        # Query OpenAI API for the answer using gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the GPT-3.5 model
            messages=[{"role": "user", "content": question}]
        )

        answer = response['choices'][0]['message']['content'].strip()  # Extract the answer
        return jsonify({'answer': answer})  # Return the answer in JSON format
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500  # Return error if OpenAI API fails

if __name__ == '__main__':
    app.run(debug=True)
