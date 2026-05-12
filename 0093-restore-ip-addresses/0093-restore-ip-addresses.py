class Solution:
    def restoreIpAddresses(self, s: str):
        
        result = []
        
        def backtrack(start, path):
            
            # If 4 parts are formed
            if len(path) == 4:
                
                # All digits must be used
                if start == len(s):
                    result.append(".".join(path))
                
                return
            
            # Try lengths 1 to 3
            for length in range(1, 4):
                
                if start + length > len(s):
                    break
                
                part = s[start:start + length]
                
                # Skip leading zeros
                if len(part) > 1 and part[0] == '0':
                    continue
                
                # Must be <= 255
                if int(part) <= 255:
                    backtrack(start + length, path + [part])
        
        backtrack(0, [])
        
        return result
        