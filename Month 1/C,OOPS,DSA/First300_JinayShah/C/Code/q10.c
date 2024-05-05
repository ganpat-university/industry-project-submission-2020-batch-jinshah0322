#include<stdio.h>
#include<string.h>
void main(){
    char string[100];
    scanf("%s",&string);
    int length = strlen(string);
    char stringrev[100];
    int j=0;
    for(int i=length-1;i>=0;i--){
        stringrev[j] = string[i];
        j++;
    }
    if(strcmp(string,stringrev)){
        printf("It is not");
    } else{
        printf("It is palindrome");
    }
}
