from flask import Flask, request, jsonify, render_template
import openai
from flask_cors import CORS  # Import CORS to handle cross-origin requests

app = Flask(__name__)

# Enable CORS for all routes (use this for local testing or different ports)
CORS(app)

# Set your OpenAI API key securely (avoid hardcoding in production)
openai.api_key = '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'  # Replace with your actual OpenAI API key

@app.route('/')
def index():
    return render_template('index.html')  # Render the frontend page

@app.route('/ask', methods=['POST'])
def ask():
    try:
        question = request.json.get('question')  # Get the question from JSON
        if not question:
            return jsonify({'error': 'No question provided'}), 400  # Return error if no question

        # Query OpenAI API for the answer using GPT-3.5 (or GPT-4)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the GPT-3.5 model
            messages=[{"role": "user", "content": question}]
        )

        answer = response['choices'][0]['message']['content'].strip()  # Extract the answer from the response
        return jsonify({'answer': answer})  # Return the answer in JSON format
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500  # Return error if OpenAI API fails

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
