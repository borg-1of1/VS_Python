# Modify the code below:
"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random

articles = input("Enter the file name for articles: ")

nouns = input("Enter the file name for nouns: ")

verbs = input("Enter the file name for verbs: ")

prepositions = input("Enter the first file name for prepositions: ")

def sentence():
    """Builds and returns a sentence."""    
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(getWords(articles)) + " " + random.choice(getWords(nouns))

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(getWords(verbs)) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(getWords(prepositions)) + " " + nounPhrase()

def getWords(file1):
    """Builds a list of words based on name of input file."""            
    my_file = open(file1,"r")
    data = my_file.read()        
    if(file1 == 'articles.txt'):
        articles = data.replace('\n',' ').split(' ')            
        return articles
    if(file1 == 'nouns.txt'): 
        nouns = data.replace('\n',' ').split(' ')             
        return nouns          
    if(file1 == 'prepositions.txt'):
        prepositions = data.replace('\n',' ').split(' ')             
        return prepositions
    if(file1 == 'verbs.txt'):
        verbs = data.replace('\n',' ').split(' ')           
        return verbs      
    my_file.close()             
    

def main():
    """Allows the user to input the number of sentences
    to generate."""    
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


# The entry point for program execution
if __name__ == "__main__":
    main()
