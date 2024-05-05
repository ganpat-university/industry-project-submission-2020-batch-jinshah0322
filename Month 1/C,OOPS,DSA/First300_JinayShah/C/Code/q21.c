#include<stdio.h>
#include<math.h>
void main(){
    int n,armstrong=0;
    int len=0;
    scanf("%d",&n);
    int original=n,compare=n;
    while (n!=0)
    {
        n=n/10;
        len++;
    }
    while (original!=0)
    {
        armstrong+=pow(original%10,len);
        original=original/10;
    }
    if(compare==armstrong){
        printf("It is an armstrong number");
    } else{
        printf("It is not");
    }
}   