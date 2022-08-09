# Sentiment-Analysis
Sentence/Text Classification Using Twitter Dataset

Twitter sentiment analysis model that helps to overcome the challenges of identifying the 
sentiments of the tweets.
The necessary details regarding the dataset are:
  This is the sentiment140 dataset. It contains 1,600,000 tweets 
  extracted using the twitter api . The tweets have been annotated (0 = negative, 4 = positive) and they can be used to detect sentiment .
  
Methods use for Pre-processing the text:
1. Casing
   Converting letter to lower case or upper case
2. Noise removal (eliminating unwanted characters)
   Html bags
   Puncutaion marks
   Contractions
   hashtags
   Special character
   Emojis
   number
   White spaces and etc
3. Tokenization
    Turning all tweets into token and all those tokens would be words that are separated by spaces in the text
4. Stopword Removal
   Removal of the word which do not make sense.
   A list of stop word provided by nltk library.
5. Text Normalization(Stemming and Lemmatization)
  Stemming – eliminates affixes(prefixes,suffixes,infixes) from a word in order to obtain a word stem
  Example : From of the word “Interact”
  Interact
  Interacting →Interact
  Interacted→Interact
  Interactions→Interact
  Interaction→Interact
  Lemmatization – Stemming sometimes loses the actual meaning of the lemmatization reduces the inflected word properly by ensuring the its morphological analysis.
  Example :
  Better→Good
  Runs/Running/Ran → Run
