import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = list(range(1, 1000001))
target = 987654

start = time.time()
linear_result = linear_search(arr, target)
end = time.time()
print("Linear Search: index =", linear_result, "time =", end - start, "seconds")

start = time.time()
binary_result = binary_search(arr, target)
end = time.time()
print("Binary Search: index =", binary_result, "time =", end - start, "seconds")
