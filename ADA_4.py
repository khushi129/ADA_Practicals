import time

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

n = 4
print("Number is :",n)
start = time.time()
iter_result = factorial_iterative(n)
end = time.time()
print("Iterative Factorial:", iter_result)
print("Time (iterative):", end - start, "seconds")

start = time.time()
rec_result = factorial_recursive(n)
end = time.time()
print("Recursive Factorial:", rec_result)
print("Time (recursive):", end - start, "seconds")
