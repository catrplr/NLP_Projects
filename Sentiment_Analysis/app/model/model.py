import pickle
import re
from pathlib import Path
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/model.pkl", "rb") as f:
    model = pickle.load(f)

def model_predict(text):
    tokenizer = Tokenizer(oov_token='<OOV>')
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, padding='post', maxlen=train_padded.shape[1])
    prediction = model.predict(padded_sequence)
    if (prediction > 0.5):
        return ("Sarcastic")  
    else:
        return ("Not Sarcastic")