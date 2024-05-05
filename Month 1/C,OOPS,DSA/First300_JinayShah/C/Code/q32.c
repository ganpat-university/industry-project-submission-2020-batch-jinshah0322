#include<stdio.h>
#include<string.h>
void main(){
    char str[100];
    int count=0;
    gets(str);
    for(int i=0;i<strlen(str);i++){
        if(str[i] == ' '){
            count++;
        }
    }
    printf("%d",count);
}