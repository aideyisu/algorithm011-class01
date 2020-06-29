class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 额外数组的方法
        n = len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]
        # 优化了好几遍才变成的这个样子QAQ
        # 翻转数组
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        # 感想:Python切片用的还不够好啊Otz

        # 环状替换
        n, count = len(nums), 0
        k %= n
        for start in range(n):
            current = start
            prev = nums[start]
            while True:
                next = (current + k) % n
                temp = nums[next]
                nums[next] = prev
                prev = temp
                current = next
                count += 1
                if start == current:
                    break
            if count >= n:
                break
        # 真的是太厉害了!