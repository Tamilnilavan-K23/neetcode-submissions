class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        r=1
        while l < len(nums):
            if nums[l] == nums[r]:
                if abs(l-r) <= k: return True
                r+=1
            l+=1
        return False