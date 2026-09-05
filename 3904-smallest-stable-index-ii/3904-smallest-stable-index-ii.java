class Solution {
    public int firstStableIndex(int[] nums, int k) {
        int n = nums.length;
        int[] Max =new int[n];
        int[] Min=new int[n];
        Max[0] = nums[0];
        for (int i =1;i<n;i++) {
            Max[i] = Math.max(Max[i -1], nums[i]);
        }
        Min[n - 1] = nums[n - 1];
        for (int i=n-2;i>=0;i--) {
            Min[i]=Math.min(Min[i +1], nums[i]);
        }

        for (int i=0;i<n;i++) {
            if (Max[i]-Min[i] <= k) {
                return i;
            }
        }

        return -1;
    }
}