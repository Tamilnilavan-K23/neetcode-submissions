class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0 
        n=len(prices)
        for i in range(n):
            for j in range(i+1,n):
                num=prices[j]-prices[i]
                if num > profit : profit = num
        return profit 