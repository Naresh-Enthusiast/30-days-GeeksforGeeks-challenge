class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,N):
        # your code here
        if N == 1:
            return [1]
        elif N == 2:
            return [1,1]
        
        fib = [1,1]
        for i in range(2,N):
            fib.append(fib[i-1] + fib[i-2])
        return fib