import argparse
import logging
import random
import sys

import store
import markov

_logger = logging.getLogger(__name__)

def main():
	arg_parser = argparse.ArgumentParser()
	sub_parser = arg_parser.add_subparsers()
	arg_parser.add_argument('--database', default=':memory:')
	arg_parser.add_argument('--n', default=3, type=int)

	train_parser = sub_parser.add_parser('train')
	train_parser.add_argument('file', nargs='+', type=argparse.FileType())
	train_parser.set_defaults(func=train_by_plain_text)

	# generate_parser = sub_parser.add_parser('generate')
	# generate_parser.add_argument('--lines', default=1, type=int)
	# generate_parser.add_argument('--seed-word')
	# generate_parser.add_argument('--no-auto-punctuation', action='store_true')
	# generate_parser.add_argument('--max-words', type=int, default=30)
	# generate_parser.set_defaults(func=generate)

	# next_word_parser = sub_parser.add_parser('next')
	# next_word_parser.add_argument('word1')
	# next_word_parser.add_argument('word2', nargs='?')
	# next_word_parser.set_defaults(func=next_word)

	args = arg_parser.parse_args()

	logging.basicConfig(level=logging.INFO)

	store = tellnext.store.SQLiteStore(path=args.database)
	model = tellnext.model.MarkovModel(store=store)

	model = markov.MarkovChain(file=args.file, args.n)
	
	args.func(args, model)


def train(args, model, lines, lower_case=True):
	count = 0

	trigrams = tellnext.training.process_trigrams(lines, lower_case=lower_case)

	for index, trigrams_group in enumerate(tellnext.util.group(trigrams, size=10000)):
		model.train(trigrams_group)

		count += len(trigrams_group)
		_logger.info('Processed %d trigrams', count)

		if index % 100 == 0 and args.limit_model and \
				model.store.count() > args.limit_model * 2:
			model.store.trim(args.limit_model)

	model.store.trim(args.limit_model)

def next_word(args, model):
	if args.word2:
		word_1 = args.word1
		word_2 = args.word2
	else:
		word_1 = None
		word_2 = args.word1

	trigram_model = model.get_trigram_model(word_1, word_2)

	for word, score in trigram_model.most_common():
		print(word, score)
