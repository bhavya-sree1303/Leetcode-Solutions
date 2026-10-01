bool checkMove(char** board, int boardSize, int* boardColSize, int rMove, int cMove, char color) {
    char opposite;

    if (color == 'B')
        opposite = 'W';
    else
        opposite = 'B';

    int directions[8][2] = {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1},
        {-1, -1},
        {-1, 1},
        {1, -1},
        {1, 1}
    };

    for (int i = 0; i < 8; i++) {
        int r = rMove + directions[i][0];
        int c = cMove + directions[i][1];
        int count = 0;

        while (r >= 0 && r < 8 && c >= 0 && c < 8 &&
               board[r][c] == opposite) {
            count++;

            r += directions[i][0];
            c += directions[i][1];
        }

        if (count > 0 &&
            r >= 0 && r < 8 && c >= 0 && c < 8 &&
            board[r][c] == color) {
            return true;
        }
    }

    return false;
}