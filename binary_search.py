# BINARY SEARCH
# O(logn)
'''
algorithm that finds an item in a sorted list by continually dividing that list in half
depending on whether the guess is higher or lower than the item being searched for

1. define method with parameters of total list and item you're searching for
2. set parameters of low and high to keep track of where the search will occur in the list
3. set a while loop that occurs while the sought after item has not been identified
4. inside the while loop check the middle element while dividing the list size in half depending on if the number is higher or lower
5. also inside the while loop have a coniditonal that checks if the guess is the item return the found  item
6. create another conditional that checks if the guess is higher than them item return guess is too high
7. else guess is too low
8. set a return of None which would indicate the item does not exist
'''

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] < item:
            low = mid + 1
        elif arr[mid] > item:
            high = mid - 1
        else:
            return mid
    return None

arr = [1, 3, 5, 7, 9]
item = 9
result = binary_search(arr, item)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list")
