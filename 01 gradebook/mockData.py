import string
import random
import pandas as pd

def randomID(length):
    id = str("")

    for i in range(length):
        idSub = str(random.randint(0, 9))
        id = id[:i] + idSub
    
    return id

def randomName():
    name = str("")
    lastName = str("")
    lettersName = random.randint(3, 6)
    letterLastName = random.randint(4, 10)

    letter = string.ascii_letters

    for i in range(lettersName):
        name = name[:i] + random.choice(letter)
    for i in range(letterLastName):
        lastName = lastName[:i] + random.choice(letter)
    
    return [name, lastName]

def randomGrade():
    mid = random.randint(0, 50)
    final = random.randint(0, 50)

    return [mid, final]

allStudent = list(range(0, 100))

for i in range(len(allStudent)):
    newStudent = [
        randomID(8),
        randomName()[0],
        randomName()[1],
        randomGrade()[0],
        randomGrade()[1]
    ]
    allStudent[i] = newStudent
    