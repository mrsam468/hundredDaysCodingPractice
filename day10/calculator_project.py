import art

print(art.logo)
def add_num(num1,num2):
    return num1+num2
def multiply_num(num1,num2):
    return num1*num2
def divide_num(num1,num2):
    return num1/num2
def multiply(num1,num2):
    return num1*num2
signs = {
    "+" : add_num,
    "-" : multiply_num,
    "*" : divide_num,
    "/" : multiply,
}

def calculator():
    total = 0
    first_number = int(input("Enter the first number: "))
    wants_to_continue = True
    while wants_to_continue:
        sign = input("+\n-\n/\n*\nchose a sign")
        second_number = int(input("enter the second number: "))
        answer = signs[sign](first_number,second_number)
        print(answer)
        total = total + answer
        choice = input(f"Do you want to continue adding {total}? (y/n): ")
        if choice == "y":
            first_number = total
        else:
            wants_to_continue = False
            print("\n"*20)
            calculator()

calculator()