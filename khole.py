#!/usr/bin/env python
import sys
import argparse
import csv

#------------------
#
# OPTIONS
#
#------------------

parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument("-l" ,"--list", help="affiche les lits", action="store_true")
parser.add_argument("-a" , "--add", nargs="*", type=int, help="affiche les lits")
parser.add_argument("-c" , "--clean", help="on efface tout", action="store_true")
parser.add_argument("-s" , "--max", help="on affiche la valeur max", action="store_true")
parser.add_argument("-s" , "--min", help="on affiche la valeur min", action="store_true")
parser.add_argument("-s" , "--sum", help="on affiche la valeur total", action="store_true")
parser.add_argument("-s" , "--moy", help="on affiche la valeur moyenne", action="store_true")
parser.add_argument("-t" , "--trieeee", help="on affiche la liste en croissant", action="store_true")
parser.add_argument("-t" , "--desc", help="on affiche la liste en croissant", action="store_true")
parser.add_argument("-h" , "--help", help="on affiche le help", action="store_true")
args = parser.parse_args()

#------------------
#
# PROGRAM
#
#------------------

if args.list:
    print ('on lit le csv')
    fname = "tableau.csv"
    file = open(fname, "rb")
    try:
        reader = csv.reader(file)
        for row in reader:
            print row
    finally:
        file.close()

elif args.add:
    print('on ecrit dans le csv')
    fname = "tableau.csv"
    file = open(fname, "a")
    args = parser.parse_args()
    try:
        writer = csv.writer(file, delimiter=' ', quotechar='|')
        argu = args.add
        writer.writerow(argu)
    finally:
        file.close()

elif args.clean:
    print('on clean le fichier csv')
    fname = "tableau.csv"
    file = open(fname, "w")
    try:
        file.truncate()
    finally:
        file.close()

elif args.min:
    print('on affiche la valeur min : ')
    fname = "tableau.csv"
    file = open(fname, "rb")
    reader = csv.reader(file)
    print min(reader)

elif args.max:
    print('on affiche la valeur max : ')
    fname = "tableau.csv"
    file = open(fname, "rb")
    reader = csv.reader(file)
    print max(reader)

elif args.sum:
    print('on affiche la valeur total : ')
    total = 0
    with open('tableau.csv', 'r') as f:
        for row in csv.reader(f):
            total += float(row[0])
        print(total)

elif args.moy:
    print('on affiche la valeur total : ')
    total = 0
    moy = 0
    with open('tableau.csv', 'r') as f:
        for row in csv.reader(f):
            total += float(row[0])
            moy = moy+1
        print(total/moy)

elif args.trieeee:
    print('on trie ds en croissant ')
    fname = "tableau.csv"
    file = open(fname, "rb")
    reader = csv.reader(file)
    print sorted(reader)

elif args.desc:
    print('on trie ds en decroissant: ')
    fname = "tableau.csv"
    file = open(fname, "rb")
    reader = csv.reader(file)
    print sorted(reader, reverse=True)

elif args.help:
    print('tu peux consulter le readme pour de l aide ! ')
