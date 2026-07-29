class Solution:
    def search(self, nums: List[int], target: int) -> int:
       hm={}
       for index ,value in enumerate(nums):
            hm[index]=value

       for key,value in hm.items():
            if value == target:
                return key
       return -1