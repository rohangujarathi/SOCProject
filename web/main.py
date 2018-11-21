from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd
from keras.models import load_model
from keras.preprocessing import text, sequence
import string
app = Flask(__name__)
global model

api = Api(app)
cors = CORS(app)


class HumorDetector(Resource):
    # tokenizer = None
    def get(self, sentence):
        return {'query':sentence, 'flag': self.predict(sentence, x_tokenizer)}

    def predict(self, data, tokenizer):
        print("in the tokenizer")
        x_test = []
        temp = ''
        for i in range(0, len(data)):
            if data[i] not in string.punctuation:
                temp += data[i]
        x_test.append(temp)
        print(x_test)
        x_test_tokenized = tokenizer.texts_to_sequences(x_test)
        x_testing = sequence.pad_sequences(x_test_tokenized, maxlen=200)
        print(x_test_tokenized)
        print(x_testing)
        score = model.predict(x_testing, verbose=1)
        print(score[0][0])
        print(score[0][1])
        if score[0][0] > score[0][1]:
            return True
        else:
            return False

def create_tokeniser():
    max_features = 100
    POS_DATAPATH = 'C:/Users/rohan/Desktop/positive.csv'
    NEG_DATAPATH = 'C:/Users/rohan/Desktop/negative.csv'
    pos_train_df = pd.read_csv(POS_DATAPATH)
    neg_train_df = pd.read_csv(NEG_DATAPATH)
    pos_list = pos_train_df.values.tolist()
    neg_list = neg_train_df.values.tolist()
    # print(len(pos_list))
    # print(len(neg_list))
    train_list = pos_list + neg_list
    x = []
    for _ in train_list:
        x.append(_[0])
    tokenizer = text.Tokenizer(num_words=max_features)
    tokenizer.fit_on_texts(x)
    return tokenizer


api.add_resource(HumorDetector, '/hm/<string:sentence>')

if __name__ == '__main__':
    model = load_model("C:/Users/rohan/Desktop/CNN.h5")
    x_tokenizer = create_tokeniser()
    app.run(debug=False, threaded=False)
