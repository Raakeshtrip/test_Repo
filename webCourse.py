import os
import csv
import string

# Create the path of the file
csvpath=os.path.join('..','Resources','web_starter.csv')
csvpathwrite=os.path.join('..','Resources','web_starter_write.csv')

#Create a list and add it as a header in the 

#with open(csvpath,'w',newline='') as csvwriter:
#     csvwrite=csv.writer(csvwriter,delimiter=',')
#     csvwrite.write(['id','title','url','isPaid','price','numSubscribers','numReviews','numPublishedLectures','instructionalLevel','contentInfo','publishedTime'])


# define the list for each header
ids=['id']
title=['titile']
url=['url']
isPaid=['ispaid']
price=['price']
numSubscribers=['numSubscribers']
numReviews=['numReviews']
numPublishedLectures=['numPublishedLectures']
instructionalLevel=['instructionalLevel']
contentInfo=['contentInfo']
courselength=['courselength']
publishedTime=['publishedTime']
SubscribersPercent=['SubscribersPercent']


#Create a file object for operation
with open(csvpath,newline='',encoding='utf8')as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)
    for row in csvreader:
        title.append(row[1])
        ids.append(row[0])
        url.append(row[2])
        isPaid.append(row[3])
        price.append(row[4])
        numSubscribers.append(row[5])
        numReviews.append(row[6])
        numPublishedLectures.append(row[7])
        instructionalLevel.append(row[8])
        contentInfo.append(row[9])
        publishedTime.append(row[10])
        #SubscribersPercent.append (int(row[5])/int(row[6]) * 100)
        #courselength.append(row[9].split())

        result=zip(ids,title,url,isPaid,price,numSubscribers,numReviews,numPublishedLectures,instructionalLevel,contentInfo,publishedTime)
        resultlist=list(result)
        with open(csvpathwrite,'w',newline='') as csvwriter:
         csvwrite=csv.writer(csvwriter,delimiter=',')
         csvwrite.writerows(resultlist)
         
