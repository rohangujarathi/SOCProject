from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd
from keras.models import load_model
from keras.preprocessing import text, sequence
import string
import pickle
import numpy as np
# import itertools
# import re
# from collections import Counter

app = Flask(__name__)
# global model

api = Api(app)
cors = CORS(app)


class HumorDetector(Resource):
    vocab = None
    cnnmodel = None

    def get(self, sentence):
        if not HumorDetector.vocab:
            pickle_in = open("vocab.pickle", "rb")
            HumorDetector.vocab = pickle.load(pickle_in)
        if not HumorDetector.cnnmodel:
            HumorDetector.cnnmodel = load_model("CNN_onekernel.h5")
        return {'query':sentence, 'flag': self.predict(sentence, HumorDetector.vocab)}

    def predict(self, input, vocabulary):
        padding_word = "<PAD/>"
        sequence_length = 76
        input = input.strip()
        sentence = input.split(' ')
        num_padding = sequence_length - len(sentence)
        new_sentence = sentence + [padding_word] * num_padding
        weights = []
        for word in new_sentence:
            if word in vocabulary:
                weights.append(vocabulary[word])
            else:
                weights.append(0)
        weights = np.array([np.array(weights)])
        # print(weights)
        score = HumorDetector.cnnmodel.predict(weights)[0][0]
        # print(score)
        if score > 0.50:
            return True
        else:
            return False


api.add_resource(HumorDetector, '/hm/<string:sentence>')

if __name__ == '__main__':
    # model = load_model("CNN.h5")
    # x_tokenizer = create_tokeniser()
    app.run(debug=False, threaded=False)
