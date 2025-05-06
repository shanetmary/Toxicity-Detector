from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained toxicity detection model
toxicity_model = pipeline("text-classification", model="unitary/toxic-bert")

# Define the check_toxicity function
@app.route('/check_toxicity', methods=['POST'])
def check_toxicity():
    user_message = request.json.get('message')  # Get the message from the frontend

    # Run the toxicity check using the pre-trained model
    result = toxicity_model(user_message)

    # If the sentence is toxic, return a message
    if result[0]['label'] == 'toxic' and result[0]['score'] > 0.8:
        return jsonify({"is_toxic": True, "message": "Be respectful! This is against our policies."}), 200

    # If the sentence is clean, return the original message
    return jsonify({"is_toxic": False, "message": user_message}), 200

if __name__ == '__main__':
    app.run(debug=True)
