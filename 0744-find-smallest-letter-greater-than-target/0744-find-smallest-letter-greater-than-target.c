char nextGreatestLetter(char* letters, int lettersSize, char target) {
    int low = 0, high = lettersSize - 1;
    int ans=0;
    while(low <= high)
    {
        int mid = low + (high - low) / 2;

        if(letters[mid] > target)
        {
            ans = mid;
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    return letters[ans];
}