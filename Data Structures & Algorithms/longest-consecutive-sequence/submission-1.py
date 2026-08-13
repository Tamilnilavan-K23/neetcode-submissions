class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0 :return 0
        nums.sort()
        cur=longest=1
        for i in range(1,len(nums)):
            if nums[i] == (nums[i-1]+1):
                cur+=1
                #longest+=1
            elif nums[i] ==nums[i-1]:
                continue
            else:
                 cur=1
            longest=max(longest,cur)

        return longest  
        '''  
        result=[]
        for i in res:
            result.append(i)
        return len
        '''
