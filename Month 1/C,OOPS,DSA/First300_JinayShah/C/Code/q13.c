#include<stdio.h>
#include<string.h>
#include<math.h>
void main(){
    int binary,remainder,decimal=0,i=0;
    scanf("%d",&binary);
    while (binary!=0)
    {
        remainder=binary%10;
        decimal+=remainder*pow(2,i);
        binary=binary/10;
        i++;
    }
    printf("%d",decimal);
}