import mockData
import pandas as pd

id = list(range(0, 100))
name = list(range(0, 100))
lastname = list(range(0, 100))
mid = list(range(0, 100))
final = list(range(0, 100))

for i in range(len(mockData.allStudent)):
    id[i] = mockData.allStudent[i][0]
    name[i] = mockData.allStudent[i][1]
    lastname[i] = mockData.allStudent[i][2]
    mid[i] = mockData.allStudent[i][3]
    final[i] = mockData.allStudent[i][4]

frame = {"ID": id,
         "Name": name,
         "Last name": lastname,
         "Midterm score": mid,
         "Final score": final}

table = pd.DataFrame(frame)
table.to_csv("studentData.csv")