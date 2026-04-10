class Solution {
    public int trap(int[] height) {
        if(height==null || height.length==0){
            return 0;
        }
        int area=0;
        int left=0;
        int right=height.length-1;
        int maxLeft=height[left];
        int maxRight=height[right];
        int res=0;

        while(left<right){
            if(maxLeft<maxRight){
                left=left+1;
                maxLeft=Math.max(maxLeft,height[left]);
                res=res+maxLeft-height[left];
            }else{
                right=right-1;
                maxRight=Math.max(maxRight,height[right]);
                res=res+maxRight-height[right];
            }
        }
        return res;
        
    }
}
