import os
import csv

budget_data = os.path.join("./resources", "budget_data.csv")
output_dir = os.path.join("./output", "output.txt")

min_imth = 0
max_imth = 0
net = 0
avg = 0
term = 0
i = 1
d = 0
dlist = []

with open(budget_data, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    term = len(data)

while i < (term - 1): 
    if i == 0:
        i += 1
        net += (int(data[i][1]))
    else:
        i += 1
        d += 1
        net += (int(data[i][1]))
        dlist.append(int(data[i][1])-int(data[d][1]))
avg = round((net / term), 2)
max_imth = max(dlist)
max_smth = str(data[dlist.index(max(dlist))+2][0])
min_imth = min(dlist)
min_smth = str(data[dlist.index(min(dlist))+2][0])
davg = (round(sum(dlist)/len(dlist),2))

text = (f"""
Financial Analysis
-----------------------------------------------
Term (in mths): {term}
Net PL in Term: $ {net}
Avg PL in Term: $ {davg}
Greatest Increase: {max_smth}  $ {max_imth}
Greatest Decrease: {min_smth}  $ {min_imth}
""")

print(text)
with open(output_dir, "w") as text_file:
    print(text, file=text_file)