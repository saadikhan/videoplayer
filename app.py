from flask import Flask, request, render_template, jsonify
import openai
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Enable CORS for all routes (use in case frontend and backend are on different ports)
CORS(app)

# Set your OpenAI API key securely (avoid hardcoding in production)
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        question = request.json.get('question')  # Get the question from JSON
        if not question:
            return jsonify({'error': 'No question provided'}), 400  # Return error if no question

        # Query OpenAI API for the answer using gpt-3.5-turbo (recommended)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the GPT-3.5 model
            messages=[
                {"role": "user", "content": question}
            ]
        )

        answer = response['choices'][0]['message']['content'].strip()  # Extract the answer from the response
        return jsonify({'answer': answer})  # Return the answer in JSON format
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500  # Return error if OpenAI API fails

if __name__ == '__main__':
    app.run(debug=True)
