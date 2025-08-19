def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1
    return numbers

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

values = [64, 25, 12, 22, 11]

print("Bubble Sort:", bubble_sort(values.copy()))
print("Selection Sort:", selection_sort(values.copy()))
print("Insertion Sort:", insertion_sort(values.copy()))
print("Merge Sort:", merge_sort(values.copy()))
print("Quick Sort:", quick_sort(values.copy()))
