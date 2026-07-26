class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        res=[]

        for String in strs:
            key="".join(sorted(String))
            if key in hm:
                hm[key].append(String)
            else:
                hm[key]=[String]
        
        for key in hm:
            res.append(hm.get(key))
        
        return res