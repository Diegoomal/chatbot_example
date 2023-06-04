import numpy as np
from tensorflow.keras import utils, layers, activations, models, preprocessing

class Test_Chatbot:

    def test_example(self):

        print('a')

    def test_example(self):

        def str_to_tokens(sentence : str):
            words = sentence.lower().split()
            tokens_list = list()
            for word in words:
                tokens_list.append(tokenizer.word_index[word]) 
            return preprocessing.sequence.pad_sequences([tokens_list],
                                                        maxlen=maxlen_questions,
                                                        padding='post')

        enc_model, dec_model = make_inference_models()

        for _ in range(10):
            states_values = enc_model.predict(str_to_tokens(input('Enter question: ')))
            empty_target_seq = np.zeros((1, 1))
            empty_target_seq[0, 0] = tokenizer.word_index['start']
            stop_condition = False
            decoded_translation = ''
            while not stop_condition :
                dec_outputs, h, c = dec_model.predict([empty_target_seq] + states_values)
                sampled_word_index = np.argmax( dec_outputs[0, -1, :] )
                sampled_word = None
                for word, index in tokenizer.word_index.items():
                    if sampled_word_index == index:
                        decoded_translation += ' {}'.format(word)
                        sampled_word = word
                
                if sampled_word == 'end' or len(decoded_translation.split()) > maxlen_answers:
                    stop_condition = True
                    
                empty_target_seq = np.zeros((1, 1))  
                empty_target_seq[0, 0] = sampled_word_index
                states_values = [h, c] 

            print(decoded_translation)
