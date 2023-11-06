#create a Chatbot in python

This project involves the creation of a Python chatbot that engages in natural language conversations with users. It leverages a pretrained GPT-2 model for generating contextually relevant responses. The chatbot is accessible through a web interface built using Flask.

## Dataset Information

This project uses a Kaggle dataset that contains a collection of dialogues and conversations. The dataset provides the training data for the chatbot's language model and serves as a valuable resource for generating contextually relevant responses.
Dataset source:[Kaggle](https://www.kaggle.com/datasets/grafstor/simple-dialogs-for-chatbot)

## Technologies Used

 Python 3.6
 Flask 2.0.2
 Transformers 4.9.1
 Pandas 1.3.3

## Prerequisites

To run this chatbot project, you'll need the following prerequisites:

 Python 3.6 or higher
 Flask
 Transformers library by Hugging Face
 Pandas (for dataset handling)

## Getting Started

1. **Installation**:
    Ensure you have Python 3.6 or higher installed.
    Install Flask using `pip install Flask`.
    Install Transformers by Hugging Face with `pip install transformers`.
    Install Pandas using `pip install pandas`.

3. **Configuration*
    Set up any necessary environment variables, API keys, or configurations as specified in `.env`. 

4. **Running the Chatbot**:
          app.py

5. Access the chatbot at http://127.0.0.1:5000 in your web browser.

   Open the web interface and start interacting with the chatbot by typing messages or questions in the input box.
   After typing your message, click a "Send" button to submit your message to the chatbot.
   The chatbot will process your input using the GPT-2 model and generate a response. This response will be displayed in the chat interface, typically below your message.

## Features

    Natural Language Processing for user-friendly conversations.
    Web-based interface for easy interaction.
    Responses generated using the GPT-2 model from Hugging Face's Transformers library.



