# Predictive Text

Predictive Text using Markov Chain and ngram model.

### Prerequisites

* Python version 3.5.2 or higher
* [Coca Dataset](https://www.ngrams.info/download_coca.asp)

## Running [TODO][TMP]

``` 
usage: markov.py [-h] [-w DATASET] [-f DATA_FILE] [--test] [--train] [--coca]
                 [-m MODEL] [-n N] [-words WORDS]
                 [--predict [PREDICT [PREDICT ...]]]

usage %prog -m<model>/-d<dataset> -n<n-gram>

optional arguments:
  -h, --help            show this help message and exit
  -w DATASET            Weights to train
  -f DATA_FILE          Text file to train/test
  --test
  --train
  --coca
  -m MODEL              Trained model
  -n N                  N in N-gram
  -words WORDS          Next n words to generate
  --predict [PREDICT [PREDICT ...]]    

EXAMPLE:
	# Download non-case sensitive w3_.zip from here: https://www.ngrams.info/download_coca.asp
	# Try small first:
	python3 markov.py -m database/w3_small.db -f dataset/w3_small.txt -n 3 --train --coca
	# If It works:
	python3 markov.py -m database/w3_.db -f dataset/w3_.txt -n 3 --train --coca # Add w3_.txt to dataset folder
	python3 markov.py -m database/w3_.db -n 3 -words 1 --predict how are 
```

## Built With

* [Python](https://docs.python.org/3/)

## Authors

* **Daniel I** - [danny311296](https://github.com/danny311296)
* **Durga Akhil Mundroy** - [akhilmd](https://github.com/akhilmd)
* **Ganesh K.** - [ganesh-k13](https://github.com/ganesh-k13)
* **Rahul R Bharadwaj** - [Rahul-RB](https://github.com/Rahul-RB)


## Acknowledgments

* This is developed as a mini project for Machine Learning course.
* This code is based on implementation of [Kevin Sookocheff](https://sookocheff.com/post/nlp/ngram-modeling-with-markov-chains/).
* The SQL store is based on chfoo's [tellnext](https://github.com/chfoo/tellnext)