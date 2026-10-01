int oddCells(int m, int n, int** indices, int indicesSize, int* indicesColSize) {
    int rows[50] = {0};
    int cols[50] = {0};

    for (int i = 0; i < indicesSize; i++) {
        int r = indices[i][0];
        int c = indices[i][1];

        rows[r]++;
        cols[c]++;
    }

    int oddRows = 0;
    int oddCols = 0;

    for (int i = 0; i < m; i++) {
        if (rows[i] % 2 != 0)
            oddRows++;
    }

    for (int j = 0; j < n; j++) {
        if (cols[j] % 2 != 0)
            oddCols++;
    }

    return oddRows * (n - oddCols) +
           (m - oddRows) * oddCols;
}