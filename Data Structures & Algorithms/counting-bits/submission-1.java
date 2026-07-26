class Solution {
    static int func(int n){
        int count=0;
        while(n>0){
            int bits=n%2;
            if(bits ==1)count++;
            n/=2;
        }
        return count;
    }
    
    public int[] countBits(int n) {
        int[] res=new int[n+1];
        for(int i=0;i<=n;i++){
            int value=func(i);
            res[i]=value;
        }
        return res;
    }
}
