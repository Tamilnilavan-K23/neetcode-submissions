class Solution {
    public boolean isSubsequence(String s, String t) {
        int low=0,mid=0;
        while(low < s.length() && mid< t.length()){
            if(s.charAt(low)==t.charAt(mid)) low++;
            mid++;
        }
        if(low == s.length()) return true;
        else return false;
    }
}