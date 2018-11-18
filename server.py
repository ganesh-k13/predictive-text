from flask import Flask, request, render_template
import subprocess
import os
from predictive_text.markov import MarkovChain
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_data',methods = ['POST'])
def handle_data():
	
	word1 = request.form["1"]
	word2 = request.form["2"]
	
	m = MarkovChain("Database/w3_.db", n = 3)
	# pprint(m.query(*(options.predict[0])))
	ngram = [word1, word2]
	res = m.query(*ngram).keys() # Actual Result
	print(res)
	# word = list(res)[random.randint(0, 2)]
	# print(word, end = ' ')

	return str(dict(zip(["predict1", "predict2", "predict3"], list(res)[:3])))
    
if(__name__ == '__main__'):
    app.run(debug=True)
