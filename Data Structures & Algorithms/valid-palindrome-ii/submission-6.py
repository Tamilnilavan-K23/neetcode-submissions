class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[::-1] == s: return True

        l,r=0,len(s)-1

        while l < r:
            if s[l] != s[r]:
                leftskip=s[l+1:r+1]
                rightskip=s[l:r]
                return leftskip[::-1] ==leftskip or rightskip[::-1] ==rightskip
            l+=1
            r-=1
        return True