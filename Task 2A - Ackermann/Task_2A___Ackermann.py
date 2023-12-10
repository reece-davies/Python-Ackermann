# COMP3002 assignment - Task 2A
# Ackermann function with decoration and memoization
# Timer is commented out due to concern of failing to execute

# Memoization function (store previously calculated values)
def memoize(f):
    # Dictionary for reference input values & output value
    memo = {}
    def helper(m, n):
        # If it has not been calculated, perform ackermann function (f)
        if str(m)+':'+str(n) not in memo:            
            memo[str(m)+':'+str(n)] = f(m, n)
        return memo[str(m)+':'+str(n)]
    return helper

# Ackermann function, decorated with memoize function  
@memoize
def ackermann(m,n):
     if m == 0:
          return (n + 1)
     elif n == 0:
          return ackermann(m - 1, 1)
     else:
          return ackermann(m - 1, ackermann(m, n - 1)) 
          
#m=int(input("What is the value for m? "))
#n=int(input("What is the value for n? "))
m = 2
n = 100

print("m = ", m)
print("n = ", n)
print(ackermann(m,n))   # Expected output = 203
print(ackermann(m,n))
print(ackermann(m,n))
print(ackermann(m,n))
print(ackermann(m,n))

# To time the function (if needed)
#import timeit
#print("Time = ", timeit.timeit('ackermann(m,n)', globals=globals(), number=1), "    Value = ", ackermann(m,n))
#print("Time = ", timeit.timeit('ackermann(m,n)', globals=globals(), number=1), "    Value = ", ackermann(m,n))
#print("Time = ", timeit.timeit('ackermann(m,n)', globals=globals(), number=1), "    Value = ", ackermann(m,n))
#print("Time = ", timeit.timeit('ackermann(m,n)', globals=globals(), number=1), "    Value = ", ackermann(m,n))
#print("Time = ", timeit.timeit('ackermann(m,n)', globals=globals(), number=1), "    Value = ", ackermann(m,n))


input("Program finished. Press any key to continue.")
