import itertools as it
import string
import argparse

class FileHandle():
	def __init__(self, file_name, n):
		self.file = file_name
		self.n = n
		self.translation = str.maketrans("","", string.punctuation);
	def get_input(self):
		with open(self.file, 'rb') as f:
			words = f.readlines()
		
		for w in words:
			if(len(w) < 30):
				continue
			new = str(w)[1:].translate(self.translation);
			yield new.lower().split()[:-1]
	
	def get_n_grams(self):
		for w in self.get_input():
			its = ([iter(w[i:]) for i in range(0, self.n)])
			yield zip(*its)
			
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'usage %prog -f<file>')
	parser.add_argument('-f', dest='file', type = str, action = 'store', help='File name')
	parser.add_argument('-n', dest='n', type = int, action = 'store', help='N in N-gram')
	
	options = parser.parse_args()
	
	p = FileHandle(options.file, options.n)
	
	for i in p.get_n_grams():
		for j in i:
			print(j)
		
	