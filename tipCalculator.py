print("Welcome to Tip Calculator")
bill = float(input("Enter the total bill: "))
tip = int(input("What percentage of the tip you would like to offfer (10 12 15) : "))
people = int(input("How many people to split the bill? "))

tip_amount = tip/100
total_bill = bill + (bill*tip_amount)
print(total_bill/people)