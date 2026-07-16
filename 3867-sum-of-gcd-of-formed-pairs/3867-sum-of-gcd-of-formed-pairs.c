#include <stdio.h>
#include <stdlib.h>

int gcd(int a, int b) {
    while (b) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int cmp(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

long long gcdSum(int* nums, int numsSize) {
    int* prefix = (int*)malloc(numsSize * sizeof(int));
    
    int mx = 0;
    
    // Step 1: build prefixGcd
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > mx) mx = nums[i];
        prefix[i] = gcd(nums[i], mx);
    }
    
    // Step 2: sort
    qsort(prefix, numsSize, sizeof(int), cmp);
    
    // Step 3: pair and compute answer
    long long ans = 0;
    int left = 0, right = numsSize - 1;
    
    while (left < right) {
        ans += gcd(prefix[left], prefix[right]);
        left++;
        right--;
    }
    
    free(prefix);
    return ans;
}