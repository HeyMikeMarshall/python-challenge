import os
import csv

election_data = os.path.join(".", "election_data.csv")
output_dir = os.path.join(".", "results.txt")

## initialize results.txt
with open(output_dir, "w+") as text_file:
    print("", file=text_file)

ttl_vote = 0
candidates = []
canid = -1
tallys = []
winner = 0
compline = []

##funtion to output print lines to text file
def tolog(text):
    print(text)
    with open(output_dir, "a+") as text_file:
        print(text, file=text_file)
        
# O's! Say does that star spangled etc.
flag = (f"""
* * * * * * ---------------
 * * * * *  ---------------
* * * * * * ---------------
 * * * * *  ---------------
---------------------------
---------------------------
---------------------------

  -= Election Results =-
  
%%%%%%%%%%%%%%%%%%%%%%%%%%%
""")
#print the flag
tolog(flag)
#open election data, tally total votes and add candidates to list
with open(election_data, newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)
    for row in reader:
        ttl_vote += 1
        if row[2] not in candidates:
            candidates.append(row[2])
#print total vote to terminal        
#print total vote to text file
tolog(f"Total Votes: {ttl_vote}")
tolog(f"---------------------------")
#tally each candidate. takes a couple of seconds, this is where you appreciate the flag.
for candidate in candidates:
    tallys.append(0)
    canid += 1
    with open(election_data, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        for row in reader:
            if row[2] == candidates[canid]:
                tallys[canid] += 1
    pct = ((tallys[canid] / ttl_vote) * 100)
    if tallys[canid] > winner:
        winner = tallys[canid]
        winname = candidate
#for each candidate print that candidate data to screen and text file.
    tolog(f"{candidate}: %{round(pct, 3)} ({tallys[canid]})")
#WE GOT A WINNER! 
winlog = (f"""---------------------------
Winner: {winname}
---------------------------""")
#print the winlog to screen and text file, call it a day.
tolog(winlog)