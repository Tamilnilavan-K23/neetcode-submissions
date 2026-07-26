class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}

        for String in strs:
            key="".join(sorted(String))
            if key in hm:
                hm[key].append(String)
            else:
                hm[key]=[String]
        
        return list(hm.values())