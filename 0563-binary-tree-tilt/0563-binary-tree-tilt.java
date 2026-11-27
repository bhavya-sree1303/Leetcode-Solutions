
class Solution {

    int tilt = 0;

    public int findTilt(TreeNode root) {

        calculateSum(root);

        return tilt;
    }

    int calculateSum(TreeNode root) {

        if (root == null) {
            return 0;
        }

        int leftSum = calculateSum(root.left);
        int rightSum = calculateSum(root.right);

        tilt += Math.abs(leftSum - rightSum);

        return root.val + leftSum + rightSum;
    }
}
