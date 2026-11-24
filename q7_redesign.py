
import time

calls = 0

# Original recursive method
def original(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return original(n - 1) + original(n - 2)


# Improved iterative method
def improved(n):
    a = 1
    b = 1
    count = 0

    for i in range(2, n + 1):
        a, b = b, a + b
        count += 1

    return b, count


# Compare both methods
calls = 0
start = time.perf_counter()
old_result = original(25)
old_time = time.perf_counter() - start

start = time.perf_counter()
new_result, steps = improved(25)
new_time = time.perf_counter() - start

print("Original result:", old_result)
print("Original calls:", calls)
print("Improved result:", new_result)
print("Improved iterations:", steps)
print("Original time:", old_time)
print("Improved time:", new_time)

# Test large input
answer, steps = improved(1000)
print("1000 steps calculated successfully")
print("Number of iterations:", steps)
