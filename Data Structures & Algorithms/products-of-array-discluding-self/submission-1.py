class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=1
        count=0
        output=[]
        for num in nums :
         if num ==0 :count+=1
         else :total=total*num

        for i in nums:
            if count >= 2:
               output.append(0)

            elif count == 1:
               if i == 0: output.append(total)
               else :output.append(0)
            
            else :output.append(total//i)

        return output