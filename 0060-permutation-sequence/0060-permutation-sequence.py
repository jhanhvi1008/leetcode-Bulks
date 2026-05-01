class Solution:
    def getPermutation(self, n, k):
        import math
        
        numbers = list(range(1, n + 1))
        k -= 1  # convert to 0-based index
        result = []
        
        while n > 0:
            fact = math.factorial(n - 1)
            index = k // fact
            
            result.append(str(numbers[index]))
            numbers.pop(index)
            
            k %= fact
            n -= 1
        
        return ''.join(result)
        