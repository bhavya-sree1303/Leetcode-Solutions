int findPeakElement(int* nums, int numsSize) {
    int l=0,h=numsSize-1;
    while(l<h)
    {
       int mid=l+ (h-l) / 2;
       if(nums[mid]>nums[mid+1])
         h=mid;
       else
         l=mid+1;
    }
    return l;
}