char* longestCommonPrefix(char** strs, int S)
{
    static char prefix[300];
    int i, j;

    for(i = 0; i <=99 && strs[0][i] != '\0'; i++)
    {
        for(j = 1; j < S; j++)
        {
            if(strs[j][i] != strs[0][i] || strs[j][i] == '\0')
            {
                prefix[i] = '\0';
                return prefix;
            }
        }

        prefix[i] = strs[0][i];
    }

    prefix[i] = '\0';   
    return prefix;      
}


    
