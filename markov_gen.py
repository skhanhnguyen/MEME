import markovify
import pickle
import os


print("Loading model...")
with open(os.getcwd()+"/markov.pkl",'rb') as f:
	model = pickle.load(f)
print('Done.')

for i in range(10):
    print(model.make_sentence())