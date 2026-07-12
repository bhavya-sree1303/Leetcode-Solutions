int firstUniqueEven(int* nums, int numsSize) {
    int f[999]={0};
    for(int i=0;i<numsSize;i++)
    {
        f[nums[i]]++;
    }
    for(int i=0;i<numsSize;i++)
    {
        if(nums[i]%2==0 & f[nums[i]]==1)
           return nums[i];
    }
    return -1;
}