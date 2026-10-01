int* sumEvenAfterQueries(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int sum = 0;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 2 == 0)
            sum += nums[i];
    }

    int* answer = (int*)malloc(queriesSize * sizeof(int));

    for (int i = 0; i < queriesSize; i++) {
        int val = queries[i][0];
        int index = queries[i][1];

        if (nums[index] % 2 == 0)
            sum -= nums[index];

        nums[index] += val;

        if (nums[index] % 2 == 0)
            sum += nums[index];

        answer[i] = sum;
    }

    *returnSize = queriesSize;

    return answer;
}