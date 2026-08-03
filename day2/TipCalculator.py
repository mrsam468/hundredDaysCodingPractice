print("Welcome to the Tip Calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("what was the total tip? 10,12,15 $"))
people = int(input("how many people to split the bill? "))
bill_with_tip = tip/100*bill
total_bill = bill+bill_with_tip
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")

