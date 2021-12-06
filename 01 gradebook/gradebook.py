from numpy.lib.polynomial import poly
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import csv file
studentData = pd.read_csv("./studentData.csv")


#summary midterm and final score
grade = list(range(0, 100))

for i in range(len(studentData)):
    sum = studentData["Midterm score"][i] + studentData["Final score"][i]
    grade[i] = sum
    
studentData["Grade"] = grade

#turn score(number) in datafram to grade(letter)
grading = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "F"
}

def scoreToGrade(score):
    for criteria, letter in grading.items():
        if score >= criteria:
            return letter

newGrade = studentData["Grade"].map(scoreToGrade)

for i in range(len(studentData)):
    studentData["Grade"][i] = newGrade[i]

#histogram
gradeAmount = {
    "F": int,
    "D": int,
    "C": int,
    "B": int,
    "A": int
}

gradeList = studentData["Grade"].tolist()

for i in ["F", "D", "C", "B", "A"]:
    gradeAmount[i] = gradeList.count(i)

plt.bar(gradeAmount.keys(), gradeAmount.values())
plt.xlabel("Grade")
plt.ylabel("Amount of students")
plt.ylim(0, 100)
plt.show()