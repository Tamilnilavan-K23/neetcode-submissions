class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        n=min((len(w) for w in strs),default = 0)
        for i in range(n):
            for num in strs:
                if num[i] != strs[0][i] : 
                    return strs[0][:i]
            
        return strs[0][:n]