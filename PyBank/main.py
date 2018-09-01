import os
import csv

csvpath = os.path.join('..', '..', '..', '..', 'GitLabDemo', 'MINSTP201808DATA2',
 '03-Python', 'Homework', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

