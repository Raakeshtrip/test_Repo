print("Welcome to house of Pies")

piesinterger=[1,2,3,4]

print("1 Pecan , 2 Apple crisp ,3 Bean ,4 Banaofee")

pieslist=["","Pecan","Apple crisp","Bean", "Banaofee"]

length=len(pieslist)

choice="y"
while choice =="y":
      i = int(input("Select which pie you want: ")) 
      print(f"[{i} {pieslist[i]}]")

      choice=input(" DO you still wants to continue: y/n ")
      