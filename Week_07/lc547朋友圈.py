# 并查集简单实现

# 在内部定义查询与合并两个选项
# 每次遇到两个集合可以合并的情况便会合并


class Solution:
    def findCircleNum(self, M) -> int:
        father = [i for i in range(len(M))]

        def find(a):
            if father[a] != a: father[a] = find(father[a])
            return father[a]

        def union(a, b):
            father[find(b)] = find(a)
            return find(b)

        for a in range(len(M)):
            for b in range(a):
                if M[a][b]: union(a, b)
        for i in range(len(M)): find(i)
        return len(set(father))

