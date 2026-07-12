int majorityElement(int* nums, int numsSize) {

    int majority = 0;
    int count = 0;

    for (int i = 0; i < numsSize; i++) {

        if (count == 0)
            majority = nums[i];

        if (nums[i] == majority)
            count++;
        else
            count--;
    }

    return majority;
}