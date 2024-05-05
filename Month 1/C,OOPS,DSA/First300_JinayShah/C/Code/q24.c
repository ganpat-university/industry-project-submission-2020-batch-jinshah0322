#include<stdio.h>
void main(){
    int gcd=0,n1,n2,greatest=0;
    scanf("%d %d",&n1,&n2);
    if(n1>n2){
        greatest=n1;
    } else{
        greatest=n2;
    }
    for(int i=1;i<greatest;i++){
        if(n1%i==0){
            if(n2%i==0){
                gcd=i;
            }
        }
    }
    printf("%d",gcd);
}   