import csv
from six.moves import cPickle as pickle
import numpy as np
path_pickle = "C:/Users/Rohan/Documents/GitHub/SOCProject/Datasets/reuters.pickle"
path_csv = "C:/Users/Rohan/Documents/GitHub/SOCProject/Datasets/reuters.csv"
# updated_csv = "C:/Users/Rohan/Documents/GitHub/SOCProject/Datasets/quotes_all_updated.csv"

def main(path_pickle,path_csv):
    '''
    Code to generate CSV file from pickle file
    '''
    x = []
    list = []
    with open(path_pickle,'rb') as f:
        x = pickle.load(f)
    for line in x:
        list.append('"'+line+'"')
    with open(path_csv,'w',encoding="utf-8") as f:
        for line in list:
            f.write(line)
            f.write('\n')


    '''Code to remove author and date from quotes csv file and create a new file'''
    '''
    list2 = []
    fileobject = open(path_csv,'r')
    list = fileobject.readlines()
    fileobject.closed
    for i in range(len(list)):
        list3 =[]
        list3.append('"')
        for j in list[i]:
            if j == ';':
                flag = False
                break
            list3.append(j)
        list3.append('"')
        list2.append(''.join(list3))

    with open(updated_csv, 'w') as f:
        for line in list2:
            f.write(line)
            f.write("\n")'''

main(path_pickle,path_csv)