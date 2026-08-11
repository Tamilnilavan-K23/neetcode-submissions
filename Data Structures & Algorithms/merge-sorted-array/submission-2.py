class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #nums1.sort()
        l=r=0

        while l < m or r < n:
            if nums1[l] ==0 :
                nums1[l]=nums2[r]
                l+=1
                r+=1
            else:
                l+=1
        return nums1.sort()
        