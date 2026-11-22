import math 
import statistics

#Ask the user for 10 numbers
ten_numbers = []
while len(ten_numbers) <10:
    numbers = int(input("Enter 10 numbers"))

#Put them in a list
    ten_numbers.append(numbers)
print(f"This is list{ten_numbers}")

#Find the total of all the  numbers
sum_of_numbers = sum(ten_numbers)
print(f"This is the sum {sum_of_numbers} index")

#Find the index of the maximum number
maximum = max(ten_numbers)
max_index = ten_numbers.index(maximum)
print(f"This is the maximum number {max_index} index")

#Find the index of the minimum number
minimum = min(ten_numbers)
min_index = ten_numbers.index(minimum)
print(f"This is the minimum number{min_index}")

#Get the average
average = statistics.mean(ten_numbers)
print(f"This is the average number{average}")

#Get the median 
median = statistics.median(ten_numbers)
print(f"This is the median {median}")