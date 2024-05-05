#include<stdio.h>
void main(){
    int a;
    int factorial=1;
    scanf("%d",&a);
    for(int i=a;i>0;i--){
        factorial*=i;
    }
    printf("factorail=%d",factorial);
}
