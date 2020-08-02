class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        maxnum = float('-inf')

        def dpmax(arr, k) :
            roll_sum = arr[0]
            roll_max = roll_sum
            maxnum = float('-inf')
            for i in range(1, len(arr)) :
                if roll_sum > 0:
                    roll_sum += arr[i]
                else:
                    roll_sum = arr[i]
                if roll_sum > roll_max:
                    roll_max = roll_sum
            
            if roll_max <= k:
                return roll_max
            for l in range(len(arr)) :
                sumnum = 0
                for r in range(l, len(arr)) :
                    sumnum += arr[r]
                    if sumnum > maxnum and sumnum <= k:
                        maxnum = sumnum
                    if maxnum == k:
                        return k
            return maxnum

        for l in range(cols) :
            row_sum = [0 for _ in range(rows)]
            for r in range(l, cols) :
                for i in range(rows) :
                    row_sum[i] += matrix[i][r]
                maxnum = max(maxnum, dpmax(row_sum, k))
                if maxnum == k:
                    return k
        return maxnum
