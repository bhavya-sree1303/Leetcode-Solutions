int oddCells(int m, int n, int** indices, int indicesSize, int* indicesColSize) {
    int rows[50] = {0};
    int cols[50] = {0};

    for (int i = 0; i < indicesSize; i++) {
        rows[indices[i][0]]++;
        cols[indices[i][1]]++;
    }

    int ans = 0;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if ((rows[i] + cols[j]) % 2 == 1) {
                ans++;
            }
        }
    }

    return ans;
}