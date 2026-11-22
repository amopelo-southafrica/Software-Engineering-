
#Ask for the first number 
try:
    first_number = int(input("Enter a number"))
except ValueError:
    print("Please enter a number")
#Ask for the operation
operation = input("Which operation would you " \
"like to perform? +,-,x or /")
#Ask for the second number 
try:
    second_number = int(input("Enter a number"))
except ValueError:
    print("Please enter a number")
#Show the answer
def Calculator(first_number,second_number):
    if operation == "+":
        result= first_number + second_number
    elif operation == "x":
        result = first_number * second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "/":
        result= first_number/second_number
    return result
#Show all the calculations and answers
total_calculation = Calculator(first_number,second_number)
print(total_calculation)
#Create the file
with open("equations.txt", "w") as file:
    file.write(f"{first_number} {operation} {second_number} = {total_calculation}")

    
