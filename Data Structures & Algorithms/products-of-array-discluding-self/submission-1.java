class Solution {
    public int[] productExceptSelf(int[] nums) {
       int l=nums.length;
       int[] prefix=new int[l];
       Arrays.fill(prefix, 1);
       int[] suffix=new int[l];
       Arrays.fill(suffix, 1);
       int[] res=new int[l];
       Arrays.fill(res, 1);
       for(int i=1;i<l;i++){
        prefix[i]=prefix[i-1]*nums[i-1];
       }
       for(int i=l-2;i>=0;i--){
         suffix[i]=suffix[i+1]*nums[i+1];
       }
        for(int i=0;i<l;i++){
            res[i]=prefix[i]*suffix[i];
        }
        return res;
    }
}  
