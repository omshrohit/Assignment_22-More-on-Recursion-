# write a recursive python function  to find the   nth term of the Fibonacci series.

# Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
 
nterms=10
if nterms <=0:
    print("plese enter a positive integer")
else:
    print("fibonacci sequence:")
    for  i in range(nterms):
        print(fibonacci(i))