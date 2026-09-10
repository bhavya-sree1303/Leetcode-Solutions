
int countNodes(struct TreeNode* root, int* sum) {
    if (root == NULL)
        return 0;
    int leftSum = 0;
    int rightSum = 0;
    int leftCount = countNodes(root->left, &leftSum);
    int rightCount = countNodes(root->right, &rightSum);
    *sum = root->val + leftSum + rightSum;
    return 1 + leftCount + rightCount;
}
int averageOfSubtree(struct TreeNode* root) {
    if (root == NULL)
        return 0;

    int ans = 0;

    void dfs(struct TreeNode* node) {
        if (node == NULL)
            return;

        int sum = 0;
        int count = countNodes(node, &sum);

        if (sum / count == node->val)
            ans++;

        dfs(node->left);
        dfs(node->right);
    }

    dfs(root);

    return ans;
}