class Solution {
    public int scoreOfString(String s) {
        int count=0;
       for(int i=0;i< s.length()-1;i++){
        int v1=(int)s.charAt(i);
        int v2=(int)s.charAt(i+1);
        count+=Math.abs(v1-v2);
       }
       return count;
    }
}