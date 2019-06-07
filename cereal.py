import os
import csv
import string


# Create the path of the file
csvpath=os.path.join('..','Resources','cereal.csv')
csvpathwrite=os.path.join('..','Resources','budget_data_write.csv')

with open(csvpath,newline='',encoding='utf8')as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader,None)#to skip the header

    for row in csvreader:
        if float(row[7])>=5:
            print(row)



