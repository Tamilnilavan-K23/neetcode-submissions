class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1. Stack stores indices, not values.

        # 2. Stack contains unresolved elements.

        # 3. Current element resolves previous elements.

        # 4. Pop until the stack becomes monotonic again.
        stack=[]
        n=len(temperatures)
        res=[0]*n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                day=stack[-1] # Did the stack change? no 
                day=stack.pop()
                res[day]=i-day
            stack.append(i)
        return res