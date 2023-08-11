# Put your code here
from collections import Counter

file1 = input("Enter the input file name: ")

# Open the file in read mode
my_file = open(file1,"r")

# Read data from file
data = my_file.read()
  
# create count list to hold words and their count
count = {}

# add all of the words to a list
words = data.replace('\n',' ').split(' ')

# iterate through list to count each word
for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1   

# Sort words into alphabetical order and get rid of duplicates
sortedWords = sorted(set(count))

# Print words and their count
for word in sortedWords:     
    print(word, count[word])

