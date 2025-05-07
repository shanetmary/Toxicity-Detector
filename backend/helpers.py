# helpers.py

from transformers import pipeline

# Load the pre-trained toxicity detection model
toxicity_model = pipeline("text-classification", model="unitary/toxic-bert")

def check_toxicity(user_message):
    """Check if the provided message is toxic."""
    result = toxicity_model(user_message)

    # If the sentence is toxic and the confidence is above 0.8, return a warning
    if result[0]['label'] == 'toxic' and result[0]['score'] > 0.8:
        return {"is_toxic": True, "reason": "this message is flagged by AI due to offensive content."}

    # Otherwise, return the original message
    return {"is_toxic": False, "message": user_message}
