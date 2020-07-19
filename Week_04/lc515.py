# 栈
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            maxnum = -12345
            for _ in range(size):
                cur = queue.popleft()
                if not cur : continue
                if maxnum == -12345 or cur.val > maxnum:
                    maxnum = cur.val
                queue.append(cur.left)
                queue.append(cur.right)
            if maxnum != -12345:
                res.append(maxnum)
        return res



