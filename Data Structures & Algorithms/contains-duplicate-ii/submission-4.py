class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm={}
        for index,value in enumerate(nums):
            if value in hm:
                if abs(index-hm.get(value)) <=k: return True
            else : hm[value]=index
        return False 