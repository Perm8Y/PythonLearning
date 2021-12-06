# My 1st project for Python learning

There're 3 files including:

### mockData.py

I tried to make data for this case by:

- assign 5 status for each student: ID, Name, Last name, Midterm score and Final score
- create function to random these 5 status
- wrap 100 students and their status into list

### createDataframe-CSV.py

Assuming I received mock data as a list from somewhere. Then I:

- create variables to get each status of student
- create dictionary to contain variables of each status
- use pandas to create dataframe from dictionary
- use pandas to export dataframe as CSV file

### gradebook.py

Assumimg I recieved mock data as CSV file. Then I:
- import CSV file by pandas
- summary midterm and final score of each student and put the values into new list
- create new column of data for sum-score
- turn student's score (number) into grade (A, B, C,...) using mapping and ordinal encoding
- create histogram by matplotlib.plot
