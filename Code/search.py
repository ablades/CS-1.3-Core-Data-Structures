#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    #Time Complexity O(n)
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    #Bounds Check
    if index >= len(array):
        return None
    #Search Check
    elif array[index] is item:
        return index

    #Advance Index
    return linear_search_recursive(array, item, index+1)



    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    #Time Complexity O(log n)
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return binary_search_iterative(array, item)
    low = 0
    high = len(array) - 1
    array.sort()
    return binary_search_recursive(array, item, low, high)


def binary_search_iterative(array, item):
    #Sort array
    array.sort()
    low = 0
    high = len(array) - 1

    while True:
        #average of low and high
        guess = (low + high) // 2 

        #High is past low meaning element is not in array
        if high < low:
            return None
        #item is present
        elif array[guess] == item:
            return guess
        
        #Shift left
        if array[guess] < item:
            low = guess + 1
        #Shift Right
        else:
            high = guess - 1


def binary_search_recursive(array, item, left=None, right=None):
    
    guess = (left + right) // 2

    #base cases
    if right < left:
        return None
    elif array[guess] == item:
        return guess

    #pass on the work
    if array[guess] < item:
        return binary_search_recursive(array, item, left=guess+1, right=right)
    else:
        return binary_search_recursive(array, item, left=left, right=guess-1)
 