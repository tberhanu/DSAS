class Solution: # More and MoreOptimization
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False
        
        i = 2
        while i < sqrt(n): #  upto sqrt(n): because beyond that, all composites have already been marked.
            if is_prime[i]:
                num = i * i # More Optimization, starting at i**2, not just i
                while num < n:
                    is_prime[num] = False
                    num += i # More Optimization, incrementing by i, not just by 1
            i += 1
        
        return sum(is_prime) # Note: True and False is considered as 1, and 0 respectively



class Solution22: # More Optimization
    def countPrimes22(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False
        
        num = 2
        while num < sqrt(n): #  upto sqrt(n): because beyond that, all composites have already been marked.
            if is_prime[num]:
                i = 2
                while num * i < n:
                    is_prime[num * i] = False
                    i += 1
            num += 1
        
        return sum(is_prime) # Note: True and False is considered as 1, and 0 respectively



class Solution2:
    def countPrimes2(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False
        
        num = 2
        while num < n:
            if is_prime[num]:
                i = 2
                while num * i < n:
                    is_prime[num * i] = False
                    i += 1
            num += 1
        
        return sum(is_prime) # Note: True and False is considered as 1, and 0 respectively