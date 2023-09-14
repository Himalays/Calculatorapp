def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide,
}

def calculator():
    num1 =float (input("Enter the first number: "))
    num2 = float (input("Enter the second number: "))

    for symbol in operations:
        print(symbol)
    continue_cal = True
    while continue_cal:
        op_symbol =input("Pick a symbol")
        calcualtion_fun = operations[op_symbol]
        answer = calcualtion_fun(num1,num2)
        print(f"{num1}{op_symbol}{num2} = {answer}")
    if input(f"Type 'y' to continue calculating with a new number, else type 'n'") == 'y':
        continue_cal = True
    else:
        continue_cal = False

calculator()

