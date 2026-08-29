class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        a = sorted((x,i) for i,x in enumerate(nums))
        ans =[0]* n
        l =0
        while l<n:
            r =l
            while r + 1<n and a[r+1][0] -a[r][0]<=limit:
                r +=1
            idx = sorted(a[i][1] for i in range(l,r+1))
            for j in range(r-l+ 1):
                ans[idx[j]]=a[l+ j][0]
            l =r+1

        return ans


        