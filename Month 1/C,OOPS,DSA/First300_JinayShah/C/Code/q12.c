#include<stdio.h>
void main(){
    int a,i;
    char binary[100];
    scanf("%d",&a);
    for(i=0;a>0;i++){
        binary[i]=a%2;
        a=a/2;
    }
    for(i=i-1;i>=0;i--){
        printf("%d",binary[i]);
    }
}