# 412 Fizz Buzz 
# 目前只能想到O(n)解法
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            current = ''
            if i % 3 == 0:
                current += 'Fizz'
            if i % 5 == 0:
                current += 'Buzz'
            res.append(str(i) if current == '' else current)
        return res
