class Rodent:
    def __init__(self, name, age):
        self.hasFur = True
        self.name = name
        self.age = age

    def getName(self):
        return "Rodent " + self.name  # using instance variable

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age  # updating instance variable

    def __str__(self):
        printStr = "Rodent, Name = " + self.name
        printStr += ", Age = " + str(self.age)
        return printStr

    def __eq__(self, otherRod):
        return (self.name == otherRod.name)\
               and (self.age == otherRod.age)

    def __ne__(self, otherRod):
        return not self == otherRod

    def __le__(self, otherRod):
        """One rodent is less than another if its age is less, or its age
        is equal and its name comes before."""
        return (self.age <= otherRod.age)\
               or ((self.age == otherRod.age) and (self.name <= otherRod.name))

    def __lt__(self, otherRod):
        return (self.age < otherRod.age) \
               or ((self.age == otherRod.age) and (self.name < otherRod.name))

    def __gt__(self, otherRod):
        return otherRod < self

    def __ge__(self, otherRod):
        return otherRod <= self


ratList = [Rodent("A", 2), Rodent("B", 1), Rodent("C", 2), Rodent("B", 1)]
if ratList[0] > ratList[1]:
    print("A is bigger")
else:
    print("B is bigger")

print(ratList[1] == ratList[2], ratList[1] == ratList[3])
ratList.sort()
for rat in ratList:
    print(rat)
