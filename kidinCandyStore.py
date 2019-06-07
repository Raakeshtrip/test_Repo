# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []



for i in range(len(candyList)):
    print(f"[{i} {candyList[i]}")

print("Select a candy")

for x in range(allowance):
    selected=int(input("Which number"))
    candyCart.append(candyList[selected])

for candy in candyCart:
    print(candy)


 