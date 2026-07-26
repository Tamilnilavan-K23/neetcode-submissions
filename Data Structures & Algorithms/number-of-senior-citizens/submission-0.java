class Solution {
    public int countSeniors(String[] details) {
        int count=0;
        for(String str : details){
            int ans =Integer.parseInt(str.substring(11,13));
            if(ans>60) count++;
        }
        return count;
    }
}