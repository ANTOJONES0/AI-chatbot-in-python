from flask import Flask, render_template, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import pandas as pd

app = Flask(__name__)

# Load and preprocess Kaggle dataset
with open('dialogs.txt', 'r', encoding='utf-8') as file:
    text_data = file.read().splitlines()

# Initialize GPT-3 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Set up routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['message']

    # Use GPT-3 to generate a response
    input_ids = tokenizer.encode(user_input, return_tensors='pt')
    output = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)

    chatbot_response = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({'message': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)