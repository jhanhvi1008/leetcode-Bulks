class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces
        s = s.strip()

        # Split words and return length of last word
        return len(s.split()[-1])
        