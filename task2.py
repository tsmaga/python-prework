import csv
import os

WordsList =list()
directory = ("/home/tomek/PycharmProjects/python-prework/zadanie_1_words")
print(directory)
os.chdir(directory)
for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".txt"):
        f = open(filename)
        lines = f.read()
        WordsList.append(list(lines))
        print(WordsList)
        continue
    else:
        break

WordsList = [item for sublist in WordsList for item in sublist]
WordsList = [x.lower() for x in WordsList]
print(WordsList)

from collections import Counter

print(Counter(WordsList))

