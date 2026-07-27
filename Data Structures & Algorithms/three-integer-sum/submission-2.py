class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)-1
        nums.sort()
        res=[]
        for i in range(n):
            l=i+1
            r=n
            while l < r:
                cur=[nums[l],nums[r],nums[i]]

                if sum(cur)==0:
                    if  cur not in res:
                            res.append(cur)
                        
                if 0 > sum(cur) : l+=1
                else: r-=1
            
        return res
                