class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        n=len(temperatures)
        for i in range(n):
            cur=temperatures[i] 
            l=i+1
            while l < n:
                if cur < temperatures[l]:
                    res.append(l-i)
                    break
                l+=1
            else : res.append(0)
                
               
        return res