class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sort the word to form a key
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())