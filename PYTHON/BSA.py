
def BinarySearch(arr: list, SearchValue: int):

    start = 0
    end = len(arr) - 1

    found = False
    searchFailed = False

    while not found and not searchFailed:

        middle = (start + end)//2  

        if start >= end: searchFailed = True

        if arr[middle] == SearchValue: found = True
        elif arr[middle] > SearchValue: end = middle - 1
        else: start = middle + 1

        
    if found: print(middle)
    else: print("Not found in array")


#Change Array To Input Array
arr = [1, 2, 19, 29, 40, 50, 62, 78, 81, 99, 120]  

#Change SearchValue to the value to search
BinarySearch(arr, SearchValue=34)
