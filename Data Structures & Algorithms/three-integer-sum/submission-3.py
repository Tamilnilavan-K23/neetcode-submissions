class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()                      # Sort so we can use Two Pointers and skip duplicates.

        for i, a in enumerate(nums):

            if a > 0:
                break                    # Since array is sorted, all remaining numbers are positive -> sum can't be 0.

            if i > 0 and a == nums[i - 1]:
                continue                 # Skip duplicate first element to avoid duplicate triplets.

            l, r = i + 1, len(nums) - 1  # Fix one element, search remaining two using Two Pointers.

            while l < r:

                total = a + nums[l] + nums[r]

                if total > 0:
                    r -= 1               # Sum is too large -> move right left to decrease the sum.

                elif total < 0:
                    l += 1               # Sum is too small -> move left right to increase the sum.

                else:
                    res.append([a, nums[l], nums[r]])  # Valid triplet found.

                    l += 1
                    r -= 1               # Move both pointers to search for the next unique pair.

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1           # Skip duplicate second element to avoid duplicate triplets.

                    # Optional (many implementations also include this)
                    # while l < r and nums[r] == nums[r + 1]:
                    #     r -= 1         # Skip duplicate third element.

        return res
                