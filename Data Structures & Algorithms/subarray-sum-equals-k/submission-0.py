class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        max_count=0
        for i in range(len(nums)):
            count=nums[i]
            if count ==k : max_count+=1
            for j in range(i+1,len(nums)):
                count+=nums[j]
                if count ==k : max_count+=1
        return max_count
