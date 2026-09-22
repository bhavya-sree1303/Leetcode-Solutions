class Solution {
    public int[] findColumnWidth(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int[] ans = new int[n];

        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) {
                int length = String.valueOf(grid[i][j]).length();

                if (length > ans[j]) {
                    ans[j] = length;
                }
            }
        }

        return ans;
    }
}