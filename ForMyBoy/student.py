"""
Project 9.1
Resources to manage a student's name and test scores.
Includes methods for comparisons and testing for equality.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
        
    # Write method definitions here
    def __eq__(self, student2):
        return (self.name == student2.name) and (self.scores == student2.scores)

    def __lt__(self, student2):
        return (self.scores < student2.scores) or ((self.scores == student2.scores) and (self.name < student2.name))
    
    def __ge__(self, student2):
        return self == student2 or self > student2

def main():
    """A simple test."""
    students = [Student("Ken", 10), Student("Mary",10), Student("Ken",10)]
    #print(student)
    for s in students:
        for i in range(1, 6):
            s.setScore(i, 100)
        print(s)
    print(students[0]==students[1], students[0]==students[2])

if __name__ == "__main__":
    main()
