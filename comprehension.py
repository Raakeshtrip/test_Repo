import string

guest=[]

for _ in range(6):
     name= input("Please enter the name:")
     guest.append(name)

lower_cased = [guest.lower() for guest in guest]

title_Cased = [guest.title() for guest in lower_cased]

print(title_Cased)

invitess= [f"Dear{guest},please Come" for guest in title_Cased]

print(invitess)