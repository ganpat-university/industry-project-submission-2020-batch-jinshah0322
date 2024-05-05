#include<stdio.h>
#include<string.h>
void main(){
    char str1[100];
    scanf("%s",&str1);
    int count=0;
    for(int i=0;i<strlen(str1);i++){
        count++;
    }
    printf("%d",count);
}