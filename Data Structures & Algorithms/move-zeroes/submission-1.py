class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        while 0 in nums:
            count+=1
            nums.remove(0)
        
        for _ in range(count):
            nums.append(0)
        
        