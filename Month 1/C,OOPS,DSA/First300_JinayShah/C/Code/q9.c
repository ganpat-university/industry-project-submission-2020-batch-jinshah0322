#include<stdio.h>
void main(){
    int a,reversed=0,remainder=0;
    scanf("%d",&a);
    while (a!=0)
    {
        remainder=a%10;
        reversed=reversed*10+remainder;
        a=a/10;
    }
    printf("%d",reversed);
}
