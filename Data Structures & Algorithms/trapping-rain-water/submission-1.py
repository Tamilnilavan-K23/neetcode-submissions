class Solution:
    def trap(self, height: List[int]) -> int:
        if not  height:
            return 0

        n=len(height)
        area=0
        for i in range(n):
            leftmax=rightmax=height[i]

            for j in range(i):
                leftmax=max(height[j],leftmax)
            
            for j in range(i+1,n):
                rightmax=max(height[j],rightmax)

            area+=min(leftmax,rightmax)-height[i]
        
        return area

