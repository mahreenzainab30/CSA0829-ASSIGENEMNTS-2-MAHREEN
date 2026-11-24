
from functools import lru_cache

calls = 0

# Normal recursion
def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# Recursion with memoization
calls = 0

@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


print("Number of ways:")

for i in range(1, 7):
    print(i, "steps:", ways_memo(i))

calls = 0
print("Memoized answer for 25:", ways_memo(25))
print("Memoized calls:", calls)


# Iterative method
def ways_loop(n):
    a = 1
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


print("Iterative answer for 1000:", ways_loop(1000))
