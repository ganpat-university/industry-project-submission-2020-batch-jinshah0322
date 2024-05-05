#include<stdio.h>
void main(){
    int n,factors[100],sum;
    scanf("%d",&n);
    int j=0;
    for(int i=1;i<n;i++){
        if(n%i==0){
            factors[j]=i;
            j++;
        }
    }
    factors[j]=999999999;
    for(int i=0;factors[i]!=999999999;i++){
        sum+=factors[i];
    }
    if(sum==n){
        printf("\nIt is a perfect number");
    } else{
        printf("\nIt is not");
    }
}   