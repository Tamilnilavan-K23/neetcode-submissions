class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm={}
        for num in nums:
            if num in hm:
                hm[num]=(hm.get(num))+1
            else:
                hm[num]=1

        for key,value in hm.items():
            if value >=2:
                return key

        return -1