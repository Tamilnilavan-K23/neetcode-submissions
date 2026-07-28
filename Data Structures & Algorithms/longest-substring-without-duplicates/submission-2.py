class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0

        for i in range(len(s)):
            num=set()
            for j in range(i,len(s)):
                if s[j] in num:
                    break
                num.add(s[j])
            
            res=max(res,len(num))
        
        return res