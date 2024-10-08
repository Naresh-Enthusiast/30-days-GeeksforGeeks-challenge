class Solution:
    def fib (self,N):
        if N == 0:
            return 0
    
    # Initializing the first two Fibonacci numbers
        a, b = 0, 1
    
    # Iterating to calculate Fibonacci numbers up to N
        for _ in range(2, N + 1):
            a, b = b, (a + b) % 10  # Only keeping the last digit of Fibonacci numbers
    
        return b if N > 0 else a