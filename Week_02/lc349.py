class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1,n2=collections.Counter(nums1),collections.Counter(nums2)
        res=[]
        for i in n1:
            tmp=min(n1[i],n2[i])
            if tmp>0:
                res.append(i)
        return re
