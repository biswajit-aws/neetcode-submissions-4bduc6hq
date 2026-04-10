class Solution {
     public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        int[] result = new int[k];
        for (int i = 0; i < 1; i++) {
            for (int num : nums) {
                count.put(num, count.getOrDefault(num, 0) + 1);
            }
        }
        Set<Map.Entry<Integer, Integer>> entryset = count.entrySet();
        List<int[]> arr = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : entryset) {
            arr.add(new int[]{entry.getValue(), entry.getKey()});
            arr.sort((a, b) -> b[0] - a[0]);

        }
        for (int i = 0; i < k; i++) {
            result[i] = arr.get(i)[1];
        }
        return result;


    }
}