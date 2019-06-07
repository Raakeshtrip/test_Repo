import os
import csv
import string


# Create the path of the file
csvpath=os.path.join('..','Resources','budget_data.csv')
csvpathwrite=os.path.join('..','Resources','budget_data_write.csv')

totalMonth=[]
periodsum=0
totalprofitloss=[]
nettotal=0
i=0
j=0

with open(csvpath,'r',newline='',encoding='utf8') as budgetfile:
     csvreader=csv.reader(budgetfile,delimiter=',')
     print(csvreader)
     for row in csvreader:
         totalMonth.append(row[0])
         totalprofitloss.append(row[1])
         
#print( len(totalprofitloss))
j=len(totalprofitloss)
for i in range(j):
     #print(i)
    #print(totalprofitloss[i])
    nettotal=sum(totalprofitloss,0)
    print(nettotal)
       



