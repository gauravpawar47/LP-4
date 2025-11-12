def fibonacci_recursive(n):
    if n <= 1:
        return n  # Base cases: F(0)=0, F(1)=1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

# Driver code
n = int(input("Enter the value of N : "))
print(f"Fibonacci Iterative({n}) = {fibonacci_iterative(n)}")

# Driver code
print(f"Fibonacci Recursive({n}) = {fibonacci_recursive(n)}")

"""
INPUT

Enter the value of N : 6

OUTPUT

Fibonacci Iterative(6) = 8
Fibonacci Recursive(6) = 8
"""