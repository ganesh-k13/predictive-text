from pprint import pprint
import random
import sys
import json
import argparse
# import nltk
from store import *

class MarkovChain:

	def __init__(self, db = ':memory:', file = '', n = 3):
		self.memory = {}
		self.n = n
		self.file = file
		self.db = db
		self.store = self.__choose_store()
		self.ngrams = []
	
	def __choose_store(self):
		db_name = self.db
		if(self.n == 2):
			return Bigram(db_name)
		elif(self.n == 3):
			return Trigram(db_name)
		elif(self.n == 4):
			return Fourgram(db_name)
		elif(self.n == 5):
			return Fivegram(db_name)
		else:
			raise NotImplementedError("%d-gram not implemented"%self.n)
	
	def process_file(self):
		with open(self.file, 'r', encoding = "ISO-8859-1") as f:
			for line in f:
				self.ngrams.append(self.learn(line.split()[1:]))
		# print(self.ngrams)
		self.to_store(self.ngrams)
	
	def __learn_key(self, *key, value):
		
		if key not in self.memory:
			self.memory[key] = []

		self.memory[key].append(value)
	
	def to_store(self, ngrams):
		self.store.add_many(ngrams)
	
	def query(self, *words):
		return (self.store.get_ngram_values(*words))
	
	def learn(self, tokens):
		ngrams = [[tokens[i+j] for j in range(self.n)] for i in range(0, len(tokens) - (self.n-1))]
		
		# for ngram in ngrams:
			# self.__learn_key(*ngram[:self.n-1], value = ngram[-1])
		return ngrams[0]
		
	def next(self, *current_state):
		next_possible = self.memory.get(current_state)
		if not next_possible:
			next_possible = self.memory.keys()

		return random.sample(next_possible, 1)
		
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'usage %prog ' + '-m<model>/-d<dataset> -n<n-gram> ')
	parser.add_argument('-d', dest='dataset', type = str, action = 'store', help='Dataset to train')
	parser.add_argument('-f', dest='data_file', type = str, action = 'store', help='Text file to train')
	parser.add_argument('-m', dest='model',  type = str, action = 'store', help='Trained model')
	parser.add_argument('-n', dest='n',  type = int, action = 'store', help='N in N-gram')
	parser.add_argument('--predict', nargs = "*", dest = 'predict', action='append')
	
	options = parser.parse_args()
	
	if(options.dataset != None):
		m = MarkovChain(options.model, options.dataset, options.n)
		m.process_file()
	elif(options.model != None):
		m = MarkovChain(options.model, n = options.n)
	else:
		print(parser.usage)
		exit(0)
	if(options.predict != []):
		pprint(m.query(*(options.predict[0])))
	
	