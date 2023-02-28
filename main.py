# reference : https://www.chegg.com/homework-help/questions-and-answers/write-program-first-reads-name-input-file
# -reads-file-using-csvreader-method-file-contains--q105963881?trackid=2b2528fcc005&strackid=dd96c0c51509

import csv

file = open(input())
dictionary = {}
reader = csv.reader(file)
for row in reader:
    for words in row:
        if words.strip() in dictionary:
            dictionary[words.strip()] += 1
        else:
            dictionary[words.strip()] = 1
for words in dictionary:
    print(words, dictionary[words])
