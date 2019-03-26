import os
import csv

budget_data = os.path.join("./resources", "budget_data.csv")
output_dir = os.path.join("./output", "output.txt")

min_imth = 0
max_imth = 0
net = 0
avg = 0
term = 0

with open(budget_data, newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)
    for row in reader:
        term += 1
        net += int(row[1])
        if max_imth < int(row[1]):
            max_imth = int(row[1])
            max_smth = row[0]
        if min_imth > int(row[1]):
            min_imth = int(row[1])
            min_smth = row[0]
avg = round((net / term), 2)


text = (f"""
Financial Analysis
-----------------------------------------------
Term (in mths): {term}
Net PL in Term: $ {net}
Avg PL in Term: $ {avg}
Greatest Increase: {max_smth}  $ {max_imth}
Greatest Decrease: {min_smth}  $ {min_imth}
""")

print(text)
with open(output_dir, "w") as text_file:
    print(text, file=text_file)