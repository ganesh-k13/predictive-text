#!/bin/bash

for i in `seq 1990 1 2012`; do python3 markov.py -w database/coca/w_acad_2.db -f dataset/coca/w_acad_$i.txt --train -n 2; done
for i in `seq 1990 1 2012`; do python3 markov.py -w database/coca/w_fic_2.db -f dataset/coca/w_fic_$i.txt --train -n 2; done
for i in `seq 1990 1 2012`; do python3 markov.py -w database/coca/w_mag_2.db -f dataset/coca/w_mag_$i.txt --train -n 2; done
for i in `seq 1990 1 2012`; do python3 markov.py -w database/coca/w_news_2.db -f dataset/coca/w_news_$i.txt --train -n 2; done
for i in `seq 1990 1 2012`; do python3 markov.py -w database/coca/w_spok_2.db -f dataset/coca/w_spok_$i.txt --train -n 2; done