int totalNumbers(int* digits, int digitsSize) {
    int count[10] = {0};
    int ans = 0;
    for (int i = 0; i < digitsSize; i++) {
        count[digits[i]]++;
    }
    for (int a = 1; a <= 9; a++) {
        for (int b = 0; b <= 9; b++) {
            for (int c = 0; c <= 8; c += 2) {
                if (count[a] == 0)
                    continue;
                count[a]--;
                if (count[b] == 0) {
                    count[a]++;
                    continue;
                }
                count[b]--;
                if (count[c] > 0)
                    ans++;
                count[b]++;
                count[a]++;
            }
        }
    }
    return ans;
}