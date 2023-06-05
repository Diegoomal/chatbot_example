import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras import utils, layers, activations, models, preprocessing

class Test_Chatbot:

    def test_example(self):

        print('a')

    def test_example(self):

        print('\n')

        encoder_input_data = None
        with open('src/artifacts/encoder_input_data.pkl', 'rb') as file:
            encoder_input_data = pickle.load(file)

        print(f'encoder_input_data.shape: {encoder_input_data.shape}')

        decoder_input_data = None
        with open('src/artifacts/decoder_input_data.pkl', 'rb') as file:
            decoder_input_data = pickle.load(file)

        print(f'decoder_input_data.shape: {decoder_input_data.shape}')

        decoder_output_data = None
        with open('src/artifacts/decoder_output_data.pkl', 'rb') as file:
            decoder_output_data = pickle.load(file)

        print(f'decoder_output_data.shape: {decoder_output_data.shape}')

        model = load_model('src/artifacts/trained_model.h5')

        print('\n')
