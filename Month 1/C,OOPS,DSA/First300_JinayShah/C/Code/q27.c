#include<stdio.h>
#include<string.h>
void main(){
    char str[100],rev[100];
    int j=0;
    scanf("%s",&str);
    for(int i=strlen(str)-1;i>=0;i--){
        rev[j]=str[i];
        j++;
    }
    printf("%s",rev);
}   