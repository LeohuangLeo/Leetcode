#509
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        lis = [0,1]
        counter = 2
        while counter != N:
            lis.append(lis[counter-1]+lis[counter-2])
            counter += 1 
        
        return lis[N-1]+lis[N-2]
