int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {

    int i = 0;
    int j = numbersSize - 1;

    int* res = (int*)malloc(2 * sizeof(int));

    while(i < j)
    {
        if(numbers[i] + numbers[j] == target)
        {
            res[0] = i + 1;
            res[1] = j + 1;
           *returnSize = 2;

            return res;
        }
        else if(numbers[i] + numbers[j] < target)
        {
            i++;
        }
        else
        {
            j--;
        }
    }
    return NULL;
}