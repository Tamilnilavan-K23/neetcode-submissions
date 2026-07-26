class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        res=[]
        nums.sort(key=lambda x: x[0])
        cur=nums[0]
        for num in nums[1:]:
            if cur[1] >= num[0]:
                start=num[0] if cur[0] > num[0] else cur[0]
                end=num[1] if  cur[1] < num[1] else cur[1]
                cur=[start,end]
            else:
                res.append(cur) 
                cur=num
        res.append(cur)
        return res