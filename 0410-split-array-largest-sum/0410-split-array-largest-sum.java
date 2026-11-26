
class Solution {
    public int splitArray(int[] nums, int k) {

        int low = 0;
        int high = 0;

        for (int i = 0; i < nums.length; i++) {
            low = Math.max(low, nums[i]);
            high += nums[i];
        }

        int ans = high;

        while (low <= high) {

            int mid = low + (high - low) / 2;

            int count = 1;
            int sum = 0;

            for (int i = 0; i < nums.length; i++) {

                if (sum + nums[i] <= mid) {
                    sum += nums[i];
                }
                else {
                    count++;
                    sum = nums[i];
                }
            }

            if (count <= k) {
                ans = mid;
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }

        return ans;
    }
}
