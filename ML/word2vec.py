import csv
import gensim
import logging
import numpy as np

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# csvpath = 'C:/Users/Rohan/Documents/GitHub/SOCProject/Datasets/shortjokes.csv'
# csvpath = uploaded['Merged_Dataset.csv']
csvpath = 'ajjaypal/Merged_Dataset.csv'

class mysentences(object):
    
    def __init__(self, dirname):
       self.dirname = dirname
    def __iter__(self): 
        i=0
        file_reader = open(csvpath, 'r')
        read = csv.reader(file_reader)
        for line in read:
            i+=1
            yield line[1].lower().split()

sentences = mysentences(csvpath)
print(sentences)
for i in sentences:
    print("xyz")
    print(i)

model = gensim.models.Word2Vec(sentences, min_count = 30, iter = 5, window = 10, sample = 1e-3, size = 100)
print("hi ajay")
print(model.wv['Beginning'])

print(model.wv.index2word[39])
# print(model.wv[Makes])
print(len(model.wv.vocab))
print(model.wv)
# print(model.wv.doesnt_match("Broken Soldered Choice Child".split()))
# model.wv.similarity('Beginning', 'Ending')
'''
def read_data(filename):
    """Extract the first file enclosed in a zip file as a list of words."""
    list = []
    file_reader = open(csvpath, 'r', encoding="utf-8")
    read = csv.reader(file_reader)
    for line in read:
        list += (line[1].split())
    return list

def convert_data_to_index(string_data, wv):
    index_data = []
    for word in string_data:
#         print(word)
        if word in wv:
            index_data.append(wv.vocab[word].index)
    return index_data

str_data = read_data(csvpath)
index_data = convert_data_to_index(str_data, model.wv)
print(str_data[:4], index_data[:4])

# convert the wv word vectors into a numpy matrix that is suitable for insertion
# into our TensorFlow and Keras models
embedding_matrix = np.zeros((len(model.wv.vocab), vector_dim))
for i in range(len(model.wv.vocab)):
    embedding_vector = model.wv[model.wv.index2word[i]]
    if embedding_vector is not None:
        embedding_matrix[i] = embedding_vector

model.train(sentences, total_examples = 2, epochs = 5)
'''
