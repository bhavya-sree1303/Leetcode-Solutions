int removeDuplicates(int* nums, int n) {
    int k=1;
    for(int i=0;i<n;i++)
    {
        if(nums[i]!=nums[k-1])
        {
            nums[k]=nums[i];
            k++;
        }
    }
    return k;
}