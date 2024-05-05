#include<stdio.h>
void main(){
    int n;
    int previous=0;
    int previous1 = 1;
    int current;
    scanf("%d",&n);
    printf("0\t1\t");
    for(int i=0;i<n-2;i++){
        current=previous+previous1;
        printf("%d\t",current);
        previous=previous1;
        previous1=current;
    }
}
