import os
import csv

csvpath = os.path.join('..', '..', '..', '..', 'GitLabDemo', 'MINSTP201808DATA2',
 '03-Python', 'Homework', 'PyPoll', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    total = 0
    row_count = 0
    
    r = [r for r in csvreader]
    col = [row[2] for row in r]
    
    row_count = len(r)

    Khan = [x for x in col if x == "Khan"]
    Correy = [x for x in col if x == "Correy"]
    Li = [x for x in col if x == "Li"]
    OTooley = [x for x in col if x == "O"+"'"+"Tooley"]
    O = "O"+"'"+"Tooley"
    
    Khan_Percent = (100*len(Khan)/(row_count))
    Correy_Percent = (100*len(Correy)/(row_count))
    Li_Percent = (100*len(Li)/(row_count))
    OTooley_Percent = (100*len(OTooley)/(row_count))
    
    candidate = ['Khan','Correy','Li',O]
    p = [Khan_Percent, Correy_Percent, Li_Percent, OTooley_Percent]
    w = max(p)
    winner = candidate[p.index(max(p))]
    
    print('Election Results')
    print(f'Total Votes: {row_count}')
    print(f'Khan: {Khan_Percent}% ({len(Khan)})')
    print(f'Correy: {Correy_Percent}% ({len(Correy)})')
    print(f'Li: {Li_Percent}% ({len(Li)})')
    print(f'{O}: {OTooley_Percent}% ({len(OTooley)})')
    print(f'Winner: {winner}')
    
    print('Election Results', file=open("output.txt", "a"))
    print(f'Total Votes: {row_count}', file=open("output.txt", "a"))
    print(f'Khan: {Khan_Percent}% ({len(Khan)})', file=open("output.txt", "a"))
    print(f'Correy: {Correy_Percent}% ({len(Correy)})', file=open("output.txt", "a"))
    print(f'Li: {Li_Percent}% ({len(Li)})', file=open("output.txt", "a"))
    print(f'{O}: {OTooley_Percent}% ({len(OTooley)})', file=open("output.txt", "a"))
    print(f'Winner: {winner}', file=open("output.txt", "a"))