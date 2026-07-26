class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        
        s1="".join(sorted(s))
        s2="".join(sorted(t))

        if s1 == s2 : return True

        return False
        