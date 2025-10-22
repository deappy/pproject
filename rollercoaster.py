print('-----------------------------------------------------')
print("Welcome to RollerCoaster")
print('-----------------------------------------------------')
height = int(input("Enter you height : "))

price=0
print('-----------------------------------------------------')
if height >=120:
    age = int(input("Enter you age : "))
    if age<=12:
        price=5
    elif age<=18:
        price=7
    else:
        price=12
    photo = input("Do you need a photogragh? (Y/N) : ")
    if(photo == "Y"):
        price+=1
    print(f"The total price is ${price}")
else:
    print("You must grow taller, try again next time!")
print('-----------------------------------------------------')