class Solution {
     public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> set=new HashSet<>();
        for(int i=0;i<nums.length-2;i++){
            for(int j=i+1;j<nums.length-1;j++){
                for(int k=j+1;k<nums.length;k++){
            if(nums[i]+nums[j]+nums[k]==0){
                List<Integer> numsList=new ArrayList<>();
                numsList.add(nums[i]);
                numsList.add(nums[j]);
                numsList.add(nums[k]);
                set.add(numsList);
            }
            }
            }

        }
        return new ArrayList<>(set);
     }
}
