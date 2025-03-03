# LINKED LISTS allow items to be inserted into memory even if they are not grouped together
'''
PROS
* good if you're going to read all items together at one time
* better for inserting items into the middle
* better for deleting an element
* allows fast inserts and deletes
CONS
* since the memory addresses of the items are unknown one would have to iterate from the first item to get the second item's memory address which would then give the third and so on.
* can only do sequential access

READING O(n), INSERTION O(1), DELETION O(1)
'''

# ARRAYS only allow items to be inserted to memory if they are grouped together
'''
PROS
* great for reading random elements because you can look up any one of them instantly
* allows random access
* allows fast reads

CONS
* elements must be grouped together 

READING O(1), INSERTION O(n), DELETION O(n)
'''

### SELECTION SORT IMPLEMENTATION
# O(n^2)
# sorting an array from smallest to largest using selection sort


def selectionSort(array, size):
    for i in range(size):
        min_index = i
        # select smallest element in each iteration
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        #swaps elements to sort the array
        (array[i], array[min_index]) = (array[min_index], array[i])

arr = [5, 4, 10, 12, 2, 11, 8, 43, -10, 16]
size = len(arr)
selectionSort(arr, size)
print('the array after sorting in ascending order is: ', arr)



