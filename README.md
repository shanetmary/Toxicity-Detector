# Toxicity-Detector
Toxicity Checker is a simple web service built using Flask to detect toxic messages in user input. It uses a pre-trained BERT model (unitary/toxic-bert) from Hugging Face for toxicity classification. This API can be used to filter out toxic messages and promote a safer environment in various applications.


**Features**
Toxicity Detection: Detects whether a message contains toxic content using a pre-trained BERT model.
Flask API: Provides an easy-to-use API endpoint for integration into other projects.


**Requirements**
Python 3.x
Flask
Hugging Face Transformers
PyTorch


Installation

1. Clone the repository
2. Navigate into the project directory: cd toxicity_detector
3. Set up a Python virtual environment: python -m venv venv
4. Activate the virtual environment:
                                    On Windows: .\venv\Scripts\activate
                                    On macOS/Linux: source venv/bin/activate
5. Install the dependencies: pip install -r requirements.txt
6. Run the Flask app: python app.py

The Flask application will start running locally at http://127.0.0.1:5000. You can interact with the API using Postman or any other HTTP client.



**API Endpoint**
POST /check_toxicity
Description: Detect if a message is toxic.
Request:
Method: POST
URL: http://127.0.0.1:5000/check_toxicity

Body (JSON):
             {
                "message": "Your message here"
             }

Response:
200 OK: The response will indicate whether the message is toxic or not:

If the message is toxic: 
                         {
                            "is_toxic": true,
                            "message": "Be respectful! This is against our policies."
                         }
f the message is clean:
                       {
                          "is_toxic": false,
                          "message": "Your message here"
                       }
