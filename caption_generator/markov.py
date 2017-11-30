from nltk.tokenize import sent_tokenize
import markovify
import re
import spacy
import os
import pickle

# nlp = spacy.load("en")

# class POSifiedTExt(markovify.Text):
#     def word_split(self, sentence):
#         return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

#     def word_join(self, words):
#         sentence = "".join(word.split("::")[0] for word in words)
#         return sentence

with open(os.getcwd()+"/captions.txt") as f:
    text = f.read()

print('Building and saving model...')
model = markovify.Text(text)
with open(os.getcwd()+"/markov.pkl",'wb') as f:
	pickle.dump(model,f)
print('Done.')
