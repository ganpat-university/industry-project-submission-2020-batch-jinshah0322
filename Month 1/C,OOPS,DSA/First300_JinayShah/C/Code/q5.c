#include<stdio.h>
void main(){
    int a,b,tmp;
    scanf("%d %d",&a,&b);
    printf("a = %d and b = %d",a,b);
    tmp = a;
    a = b;
    b = tmp;
    printf("\nAfter swapping\na = %d and b = %d",a,b);
}  
