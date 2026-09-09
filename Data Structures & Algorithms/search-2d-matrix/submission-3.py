class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''  
            if len(matrix)==1 :
            if matrix[0][0]==target: return True
            else : return False 
        '''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        
        return False