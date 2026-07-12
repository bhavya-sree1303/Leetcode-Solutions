int evalRPN(char** tokens, int tokensSize) {
    int stack[tokensSize];
    int top=-1;
    for(int i=0;i<tokensSize;i++)
    {
        char*t=tokens[i];
        if(strlen(t)==1 & (t[0]=='+' || t[0]=='-' || t[0]=='*' || t[0]=='/')){
            int a=stack[top--];
            int b=stack[top--];
            int result;
            if(t[0]=='+') result= b + a;
            else if(t[0]=='-') result=b-a;
            else if(t[0]=='*') result=b*a;
            else if (a!=0) result=b/a;
            else result=0;
            stack[++top]=result;

        }
        else
           stack[++top]=atoi(t); 
           }
    return stack[top];

}