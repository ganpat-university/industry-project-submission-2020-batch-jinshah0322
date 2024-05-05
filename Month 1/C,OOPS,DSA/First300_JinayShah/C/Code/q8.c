#include<stdio.h>
void main(){
    int a,count=0;
    scanf("%d",&a);
    for(int i=2;i<a;i++){
        if(a%i==0){
            count=1;
            break;
        }
    }
    if(count==1){
        printf("%d is not prime",a);
    } else{
        printf("%d is prime",a);
    }
}