class Solution {
    public int maxArea(int[] heights) {
        int maxHeight=0;
        int left=0;
        int right=heights.length-1;
        while(left<right){
            int leftHeight=heights[left];
            int rightHeight=heights[right];
            int currHeight=(right-left) * Math.min(leftHeight , rightHeight);
            maxHeight=Math.max(maxHeight,currHeight); 
            if(leftHeight<rightHeight) {
                left=left+1;
            }else{
                right=right-1;
            }
        }
        return maxHeight;
        
    }
}
