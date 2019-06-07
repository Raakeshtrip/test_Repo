import os
import csv
csvpath=os.path.join('..','Resources','WWE-Data-2016.csv')

def print_percentages(wrestler_Date):
    win=int(wrestler_Date[1])
    loss=int(wrestler_Date[2])
    name=str(wrestler_Date[0])
    draw=int(wrestler_Date[3])
    totalmatches=win + loss + draw
    percentofloss=loss/totalmatches * 100
    print(f"name of wrestler is {name} he won {win} , lost {loss} and draw {draw} . his lost percentage was {percentofloss}")


    # Split the data on commas
with open(csvpath,newline='',encoding='utf8')as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)





    
  