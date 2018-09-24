import time
# Normal method
start = time.time()
def fib0(n, k):
    a, b = 1, 1
    for i in range(n-2):
        a, b = b, k*a + b
    return b

print(fib0(31,4))
end = time.time()
print('Duration', end-start,'\n')

# Using dynamic programming
start = time.time()
fibocache = {}
def fib1(n, k):
    if n == 2 or n == 1:
        return 1
    if (n, k) not in fibocache:
        fibocache[(n, k)] = fib1(n-1, k) + fib1(n-2, k)*k
    return fibocache[(n,k)]

print(fib1(31,4))
end = time.time()
print('Duration', end-start,'\n')

# Without using dynamic programming
start = time.time()
def fib2(n, factor):
    if n == 2 or n == 1:
        return 1

    return factor*fib2(n-2, factor) + fib2(n-1,factor)

print(fib2(31,4))
end = time.time()
print('Duration', end-start,'\n')
