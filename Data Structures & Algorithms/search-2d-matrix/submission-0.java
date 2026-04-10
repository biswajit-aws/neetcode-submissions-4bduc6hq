class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row=matrix.length;
        int column=matrix[0].length;
        for(int i=0;i<row;i++ ){
        int start=0;
        int end=column-1;
        while(start<=end){
            int mid=start+(end-start)/2;
            System.out.println(i+" "+mid);
            if(matrix[i][mid]>target){
                end=mid-1;
            }else if(matrix[i][mid]<target){
start=start+1;
            }else{
               return true; 
            }
            
        }
    }
    return false;

    }
}
