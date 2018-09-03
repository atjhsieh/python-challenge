import os
import csv

csvpath = os.path.join('..', '..', '..', '..', 'GitLabDemo', 'MINSTP201808DATA2',
 '03-Python', 'Homework', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    total = 0
    row_count = 0
    
    r = [r for r in csvreader]
    row = [row[1] for row in r]
    rr = [rr[0] for rr in r]
    n_row = len(row)-1
    
    row_count = sum(1 for i in r)
    total = sum(int(row[i]) for i in range(0,len(row)))
    month_chg = [int(row[i+1])-int(row[i]) for i in range(n_row)]
    #avg_chg = (int(row[n_row]) - int(row[0]))/(n_row)
    avg_chg = round(sum(month_chg)/n_row,2)
    max_chg = max(month_chg)
    min_chg = min(month_chg)
    i = month_chg.index(max(month_chg))+1
    j = month_chg.index(min(month_chg))+1
    
    print('Financial Analysis')
    print(f'Total Months: {row_count}')
    print(f'Total: $ {total}')
    print(f'Average Change: $ {avg_chg}')
    print(f'Greatest Increase in Profits: {rr[i]} ($ {max_chg})')
    print(f'Greatest Decrease in Profits: {rr[j]} ($ {min_chg})')
    
