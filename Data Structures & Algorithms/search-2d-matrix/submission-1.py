class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])
        top,bottom=0,rows-1
        while top<=bottom:
            mid_row=top+((bottom-top)//2)
            if matrix[mid_row][0]>target:
                bottom=mid_row-1
            elif matrix[mid_row][-1]<target:
                top=mid_row+1
            else:
                break

        if top>bottom:
            return False
        left,right=0,cols-1

        mid_row=top+((bottom-top)//2)


        while left<=right:
            mid=left+((right-left)//2)
            if matrix[mid_row][mid]<target:
                left=mid+1
            elif matrix[mid_row][mid]>target:
                right=mid-1
            else:
                return True
        return False

            





