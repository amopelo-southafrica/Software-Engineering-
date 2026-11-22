def largest_numbers(numbers_list):
    
    if len(numbers_list) == 1:
        return numbers_list[0]

    max_of_rest = largest_numbers(numbers_list[1:])

    if numbers_list[0] > max_of_rest:
        return numbers_list[0]
    else:
        return max_of_rest

print(largest_numbers([7,9,7,5]))    
     
