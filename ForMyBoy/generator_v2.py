# Modify the code below:
"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random

articles = ("A", "THE")

nouns = ("BOY", "GIRL", "BAT", "BALL")

verbs = ("HIT", "SAW", "LIKED")

prepositions = ("WITH", "BY")

conjunctions = ("AND", "OR")

adjectives = ("RED", "HARD", "SOFT", "BLUE", "LARGE", "SMALL", "WHITE")

def sentence():
    """Builds and returns a sentence."""
    completeSentence = nounPhrase() + " " + verbPhrase() 
    if(random.random()> 0.5):
        completeSentence = completeSentence + " " + conjunction() + " " + verbPhrase()
    return completeSentence

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""    
    if (random.random()> 0.5):
        phrase = random.choice(verbs) + " " + adjective() + " " + nounPhrase()
    else:
        phrase = random.choice(verbs) + " " + nounPhrase()
    if(random.random()> 0.5):
        phrase = phrase + " " + prepositionalPhrase()
    return phrase
           

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def conjunction():
    return random.choice(conjunctions)

def adjective():
    return random.choice(adjectives)

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()
