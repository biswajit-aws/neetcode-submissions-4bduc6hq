class Solution {
     public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res=new ArrayList<>();
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        for(int i=0;i<nums.length;i++){
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }else{
                int left=i+1;
                int right=nums.length-1;
                while(left<right){
                    int sum=nums[left]+nums[right]+nums[i];
                    if(sum<0){
                        left=left+1;
                    }else if(sum>0){
                        right=right-1;
                    }else{
                       List<Integer> numList=Arrays.asList(nums[left],nums[right],nums[i]);
                       res.add(numList);
                        left=left+1;
                        while(left<nums.length-1 && nums[left]==nums[left-1]){
                            left=left+1;
                        }
                    }
                }
            }
        }
        return res;
        
        
     }
}
