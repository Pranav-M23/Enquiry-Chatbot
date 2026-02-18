from tkinter import *
import random
import json
import pickle
import numpy as np
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
import nltk
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbotmodel.h5')
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list
def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result
def handle_input():
    message = input_box.get()
    intents_list = predict_class(message)
    response = get_response(intents_list, intents)
    output_box.insert(END, "You: " + message + "\n")
    output_box.insert(END, "Bot: " + response + "\n")
    input_box.delete(0, END)
root = Tk()
root.title("JTMCOE CHAT BOT")
root.config(bg="#667EEA")

label_text = "Ask me :"
l1 = Label(root, text=label_text, background=root['background'], fg="white")
l1.place(x=3, y=10)
input_box = Entry(root, width=80,bg="#e0e0e0")
input_box.pack(padx=60, pady=10)
input_box.insert(0,"Input your query here")
def temp_text(e):
    input_box.delete(0,"end")
input_box.bind("<FocusIn>",temp_text) 
input_box.bind("<Return>",lambda event: handle_input())
output_box = Text(root, width=85, height=20,bg="#e0e0e0")
output_box.pack(padx=9, pady=9)
submit_button = Button(root, text="Submit", command=handle_input,bg="#e0e0e0")
submit_button.pack(padx=10, pady=10)
root.mainloop()