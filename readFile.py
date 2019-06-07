
import os
import csv

nameofshow =input("Write a name of show you want to know about:")
csvpath = os.path.join('..', 'Resources', 'netflix_ratings.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

   


    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    found = False
    for row in csvreader:
        if row[0]==nameofshow:
            print(row[0] + 'is rated ' + row[1] + 'With a rating of ' + row[5])
            found=True
            break
if found is False:
    print("Sorry")