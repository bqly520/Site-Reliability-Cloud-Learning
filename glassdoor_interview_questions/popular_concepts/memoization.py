# Fibonacci using memoization
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# Adding last two numbers to get to the next
def fibonacciVal(n):  
    memo = [0] * (n+1)  
    memo[0], memo[1] = 0, 1  
    for i in range(2, n+1):    
        memo[i] = memo[i-1] + memo[i-2]  
        
    return memo[n]
