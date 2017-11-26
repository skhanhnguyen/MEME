from nltk.tokenize import sent_tokenize
import markovify
import re
import spacy
import os

nlp = spacy.load("en")

class POSifiedTExt(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = "".join(word.split("::")[0] for word in words)
        return sentence

with open(os.getcwd()+"/philosopher_stone.txt",encoding='utf8') as f:
    text = f.read()

model = markovify.Text(text)

for i in range(10):
    print(model.make_sentence_with_start("The"))