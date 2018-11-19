from flask import Flask, request, render_template, jsonify
import subprocess
import os
from markov import MarkovChain
import random
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

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
	response = jsonify(dict(zip(["predict1", "predict2", "predict3"], list(res)[:3])))
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response
    
if(__name__ == '__main__'):
    app.run(debug=True)
