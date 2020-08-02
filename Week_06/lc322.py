class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [float('inf')]*(amount+1)
        # dp[0] = 0
        # # dp=[0]*(amount+1)
        # for i in range(1,amount+1):
        #     for j in coins:
        #         if i<j:
        #             continue
        #         dp[i]= min(dp[i],dp[i-j]+1)
        # return dp[-1] if dp[-1]!=float("inf") else -1

        n = len(coins)
        coins.sort(reverse=True)
        self.res = float("inf")
        
        def dfs(index,target,count):
            coin = coins[index]
            # if count>self.res:
            #     return
            if math.ceil(target/coin)+count>=self.res:
                return
            if target%coin==0:
                self.res = count+target//coin
            if index==n-1:return
            for j in range(target//coin,-1,-1):
                dfs(index+1,target-j*coin,count+j)

        dfs(0,amount,0)

        return int(self.res) if self.res!=float("inf") else -1
