char* lexGreaterPermutation(char* s, char* target) {
    int cnt[26]={0};
    int n=strlen(s);

    for(int i=0;i<n;i++)
        cnt[s[i]-'a']++;

    int i=0;

    while(i<n) {
        int x=target[i]-'a';

        if(cnt[x]==0)
            break;

        cnt[x]--;
        i++;
    }

    for(int j=(i<n?i:i-1);j>=0;j--) {
        if(j<i)
            cnt[target[j]-'a']++;

        int x=target[j]-'a';

        for(int k=x+1;k<26;k++) {
            if(cnt[k]>0) {
                cnt[k]--;

                char *ans=malloc(n+1);
                int pos=0;

                for(int p=0;p<j;p++)
                    ans[pos++]=target[p];

                ans[pos++]=k+'a';

                for(int p=0;p<26;p++) {
                    while(cnt[p]>0) {
                        ans[pos++]=p+'a';
                        cnt[p]--;
                    }
                }

                ans[pos]='\0';
                return ans;
            }
        }
    }

    return "";
}