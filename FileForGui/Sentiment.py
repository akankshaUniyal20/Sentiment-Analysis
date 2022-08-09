import pickle

import textpreprocessing as tp
# Load the vectoriser.
file1 = open("D:\\Mini_project\\SentimentalAnalysis\\FileForGui\\vectoriser-ngram-(1,2).pickle", 'rb')
vectoriser = pickle.load(file1)
# Load the LR Model.
file2 = open("D:\\Mini_project\\SentimentalAnalysis\\FileForGui\\Sentiment-LR.pickle", 'rb')
LRmodel = pickle.load(file2)

file1.close()
file2.close()

def Detector(text):
    S = tp.process_text(text)
    
    text_list=[]
    text_list.append(S)
    
    S = vectoriser.transform(text_list)
    sentiment = LRmodel.predict(S)
    text_list.pop()
    
    if(sentiment[0]==4):
        return "Positive"
    else:
        return "Negative"
