#include<stdio.h>
int main()
{
    int num,sqr,last,sqrl;
    printf("Enter a number : ");
    scanf("%d",&num);
    sqr=num*num;
    last=num%10;
    sqrl=sqr%10;
    if(last==sqrl)
    {
        printf("the number is automorphic");
    }
    else
    {
        printf("not a automorphic");
    }
return 0;
}
    
