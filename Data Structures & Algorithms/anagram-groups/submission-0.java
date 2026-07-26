class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> res=new HashMap<>();
        for(String str :strs){
            int[] count=new int[26];
            for(int i=0;i<str.length();i++){
                count[str.charAt(i)-'a']++;
            }
           String ans=Arrays.toString(count);
           res.putIfAbsent(ans,new ArrayList<>());
           res.get(ans).add(str);
        }
        return new ArrayList<>(res.values());
    }
}
