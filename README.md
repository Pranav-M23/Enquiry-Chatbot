# College Enquiry Chatbot

This is a college enquiry chatbot that can answer questions about the college. It is built using the Python programming language and the TensorFlow library.

## Prerequisites

To run this chatbot, you will need the following:

* Python 3.6 or later
* TensorFlow 2.0 or later
* The nltk library
* The tkinter library

## Installation

To install the required libraries, run the following commands:

```
pip install tensorflow
pip install nltk
pip install tkinter
```

## Usage

To run the chatbot, clone this repository and run the following command:

```
python main.py
```

The chatbot will start running and you can start asking it questions.

## Code Explanation

The code for the chatbot is divided into two files:

* `main.py`: This file contains the main code for the chatbot.
* `intents.json`: This file contains the intents and responses for the chatbot.

### main.py

The `main.py` file contains the following functions:

* `clean_up_sentence()`: This function cleans up a sentence by removing punctuation and lemmatizing the words.
* `bag_of_words()`: This function creates a bag-of-words representation of a sentence.
* `predict_class()`: This function predicts the class of a sentence.
* `get_response()`: This function gets the response for a given class.
* `handle_input()`: This function handles the input from the user.

### intents.json

The `intents.json` file contains the intents and responses for the chatbot. Each intent is represented by a JSON object with the following keys:

* `tag`: The name of the intent.
* `responses`: A list of responses for the intent.

## Step-by-Step Explanation

The following is a step-by-step explanation of how the chatbot works:

1. The user enters a question.
2. The `clean_up_sentence()` function cleans up the question by removing punctuation and lemmatizing the words.
3. The `bag_of_words()` function creates a bag-of-words representation of the question.
4. The `predict_class()` function predicts the class of the question.
5. The `get_response()` function gets the response for the predicted class.
6. The response is displayed to the user.

....


