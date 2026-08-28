class Solution:
    def lexPalindromicPermutation(self,s: str,target: str) -> str:
        from collections import Counter
        n=len(s)
        c=Counter(s)
        if sum(v%2 for v in c.values())>1:
            return ""
        m=n//2
        mid=""
        if n%2:
            for ch in c:
                if c[ch]%2:
                    mid=ch
                    break
        def make(h):
            return ''.join(h)+mid+''.join(reversed(h))
        cc=c.copy()
        h=[]
        possible=True
        for ch in target[:m]:
            if cc[ch]<2:
                possible=False
                break
            cc[ch]-=2
            h.append(ch)
        if possible:
            ans=make(h)
            if ans>target:
                return ans

        for i in range(m-1,-1,-1):
            cc=c.copy()
            possible=True

            for j in range(i):
                ch=target[j]
                if cc[ch]<2:
                    possible=False
                    break
                cc[ch]-=2

            if not possible:
                continue

            for ch in sorted(cc):
                if cc[ch]>=2 and ch>target[i]:
                    cc[ch]-=2
                    h=list(target[:i])+[ch]

                    for x in sorted(cc):
                        h += [x]*(cc[x]//2)

                    return make(h)

        return ""