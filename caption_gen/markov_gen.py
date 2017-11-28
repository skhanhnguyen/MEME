import markovify
import pickle
import os


print("Getting model...")
with open(os.getcwd()+"/markov.pkl",'wb') as f:
	pickle.dump(model,f)
print('Done.')

for i in range(10):
    print(model.make_sentence_with_start("The"))