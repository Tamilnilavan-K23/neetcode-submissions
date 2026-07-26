class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums);
        if(nums.length==0) return false;
         int next=nums[0];
         for(int i=1;i<nums.length;i++){
            if(next == nums[i]) return true;
            next=nums[i];
         }
        return false;
    }
}