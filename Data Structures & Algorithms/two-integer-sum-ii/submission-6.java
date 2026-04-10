class Solution {
     public int[] twoSum(int[] numbers, int target) {
        int i=0;
        int j=numbers.length;
        
        while(i<j-1){
            if(numbers[i]+numbers[j-1]==target){
                return new int[]{i+1,j};
            }else if(numbers[i]+numbers[j-1]>target){
                --j;
            }else{
                i++;
            }
        }
        return new int[]{-1,-1};
    }
}
