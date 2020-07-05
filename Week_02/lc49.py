class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HashMap = {}
        for i in strs:
            B = list(i)
            B.sort()
            # print(B)
            current = "".join(B)
            HashMap[current] = [i] if current not in HashMap else HashMap[current] + [i]
        return [HashMap[i] for i in HashMap] 
