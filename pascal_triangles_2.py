# https://leetcode.com/problems/pascals-triangle-ii/submissions/


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        pascal = []
        
        for rowNum in range(rowIndex+1):
            row = [None for _ in range(rowNum+1)]
            row[0],row[-1] = 1, 1
            
            for j in range(1,rowNum):
                row[j] = pascal[rowNum-1][j-1] + pascal[rowNum-1][j]
                
            pascal.append(row)
            
        return pascal[-1]