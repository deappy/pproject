print('-----------------------------------------------------')
print("Welcome to RollerCoaster")
print('-----------------------------------------------------')
age = int(input("Enter you age : "))
height = int(input("Enter you height : "))
print('-----------------------------------------------------')
if age>=12:
    if height<=120:
        print("You must grow taller, try again next time!")
    else:
        print("Enjoy your ride!!")
else:
    print("You are underage, come again next time!")
print('-----------------------------------------------------')