class Solution:
    # 思路：
    # 1、可以直接遍历找，复杂度m*n。
    # 2、可以行间遍历找，行内二分查找，复杂度m*logn。
    # 3、因为矩阵按照Z字形是严格升序的，所以如果按照Z字形排序好，可以原地二分查找。
    # 可以使用额外空间把它降维再二分；这里的技巧是通过计算将mid索引转化为矩阵的行列值索引。
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        # 两边闭合区间
        left, right = 0, m * n
        while left < right:
            mid = (left + right) // 2
            # 一维索引转化为二维索引的技巧
            mid_val = matrix[mid // n][mid % n]
            if mid_val == target: return True
            if mid_val < target:
                left = mid + 1
            elif mid_val > target:
                right = mid
        return False
