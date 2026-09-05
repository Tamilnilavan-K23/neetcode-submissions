class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        count=0
        hm={0:1}
        for num in nums:
            prefix+=num
            req=prefix-k

            if req in hm: 
                count+=hm[req]
            hm[prefix]=1+hm.get(prefix,0)
        return count