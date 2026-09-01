class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        values=set()
        l=0
        
        for r in range(len(nums)):
            if nums[r] in values: return True
            values.add(nums[r])
            if r-l >= k:values.remove(nums[l]); l+=1
        return False