class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        Table = [0] * 26

        for i in range(len(s)):
            Table[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            Table[ord(t[i]) - ord('a')] -= 1
            if Table[ord(t[i]) - ord('a')] < 0:
                return False

        return True
