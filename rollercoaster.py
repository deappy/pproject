print("Welcome to RollerCoaster")
age = int(input("Enter you age"))
height = int(input("Enter you height"))
if age>=12:
    if height<=150:
        print("You must grow taller, try again next time!")
    else:
        print("Enjoy your ride")
else:
    print("You are underage, come again next time!")