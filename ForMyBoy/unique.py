# get file to be navigated
file1 = input("Enter the first file name: ")

# Opne file in read mode
my_file = open(file1,"r")

# Read data from file
data = my_file.read()

words = filter(lambda x: x.isalpha(), data.replace('\n',' ').split(' '))

sortedWords = sorted(set(words))

for x in range(len(sortedWords)):
    print(sortedWords[x])

