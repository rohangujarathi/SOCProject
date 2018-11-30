def predict(data):
    model = load_model('/content/drive/My Drive/Colab Notebooks/CNN.h5')
    import string
    x_test = ''
    for i in range(0,len(data)):
      if data[i] not in string.punctuation:
        x_test+=data[i]
    x_test_tokenized = x_tokenizer.texts_to_sequences(x_test)
    x_testing = sequence.pad_sequences(x_test_tokenized, maxlen=200)
    score = model.predict(x_testing, verbose = 1)
    if score[0][0]>score[0][1]:
      return True
    else:
      return False