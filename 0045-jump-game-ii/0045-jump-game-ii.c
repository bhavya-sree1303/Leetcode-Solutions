int jump(int* nums, int numsSize) {
    int jumps = 0;
    int currentEnd = 0;
    int reach = 0;

    for(int i = 0; i < numsSize - 1; i++)
    {
        if(i + nums[i] > reach)
        {
            reach= i + nums[i];
        }

        if(i == currentEnd)
        {
            jumps++;
            currentEnd = reach;
        }
    }

    return jumps;
}