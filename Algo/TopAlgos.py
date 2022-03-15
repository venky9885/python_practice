# #####! Linear Search
# https://github.com/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews
def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
# ! Binary Search

#Divide and conquer
# must be sorted


def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
        # for get integer result
        mid = (high + low) // 2
        # Check if n is present at mid
        if list1[mid] < n:
            low = mid + 1
        # If n is greater, compare to the right of mid
        elif list1[mid] > n:
            high = mid - 1
        # If n is smaller, compared to the left of mid
        else:
            return mid

            # element was not present in the list, return -1
    return -1


# Initial list1
list1 = [12, 24, 32, 39, 45, 50, 54]
n = 45
# Function call
result = binary_search(list1, n)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list1")
