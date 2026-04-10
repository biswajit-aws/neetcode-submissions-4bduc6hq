class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        int i=1;
        int longestArray=1;
        int temp=1;
        if(nums.length==0){
            return 0;
        }
        while(i<nums.length){
            if(nums[i]==nums[i-1]+1){
                temp++;
            }else if(nums[i]==nums[i-1]){
                i++;
                continue;
            }else{
                longestArray=Math.max(longestArray,temp);
                temp=1;
            }
            i++;
        }
        return Math.max(longestArray,temp);
    }
}
