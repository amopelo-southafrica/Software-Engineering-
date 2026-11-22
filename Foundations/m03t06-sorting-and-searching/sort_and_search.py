list1 =[27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

def binary_search(target,items):
    low, high =0, len(items) -1

    while high >= low:
        mid = (low + high ) //2
        
        if items[mid] == target:
            return mid
        
        elif items[mid] <target:
            low = mid +1
        else: 
            high = mid -1
    return None

list1 =[27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target_item = 9 
result = binary_search(9,list1)
if result is not None: 
    print(f"Item {target_item} found at index {result}.") 
else: 
    print(f"Item {target_item} not found in the list.")