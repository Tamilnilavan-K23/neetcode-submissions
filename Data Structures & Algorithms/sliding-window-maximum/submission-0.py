class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r=0,k
        res=[]
        while r < len(nums)+1:
            max_no=max(nums[l:r])
            res.append(max_no)
            l+=1
            r+=1
        return res