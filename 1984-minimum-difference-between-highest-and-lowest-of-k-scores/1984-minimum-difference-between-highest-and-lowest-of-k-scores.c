#include<stdio.h>
#include<stdlib.h>

int compare(const void*a,const void*b)
{
    return (*(int*)a - *(int*)b);
}

int minimumDifference(int* nums, int numsSize, int k) {

    int i, j;

    if(k == 1)
        return 0;

    qsort(nums, numsSize, sizeof(int), compare);

    int mindiff = nums[k-1] - nums[0];

    for(i = 0; i <= numsSize - k; i++)
    {
        j = i + k - 1;

        if(nums[j] - nums[i] < mindiff)
        {
            mindiff = nums[j] - nums[i];
        }
    }

    return mindiff;
}