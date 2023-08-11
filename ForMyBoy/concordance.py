# Put your code here
from collections import Counter

file1 = input("Enter the input file name: ")

# Open the file in read mode
my_file = open(file1,"r")

# Read data from file
data = my_file.read()
  
# create method to coutn the unique words
count = {}

for w in data.replace('\n',' ').split(' '):
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
for word, times in count.items():
    print(word, times)

