class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        l=0
        num=set()
        for i in range(len(s)):
            while s[i] in num:
                num.remove(s[l])
                l+=1
            num.add(s[i])
            res=max(res,i-l+1)

        return res
