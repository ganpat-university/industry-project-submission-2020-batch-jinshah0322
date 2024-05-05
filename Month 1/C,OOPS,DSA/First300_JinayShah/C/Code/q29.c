#include<stdio.h>
#include<string.h>
void main(){
    char str1[100],str2[100];
    char final[100];
    scanf("%s %s",&str1,&str2);
    int j=0;
    for(int i=0;i<strlen(str1);i++){
        final[j]=str1[i];
        j++;
    }
    for(int i=0;i<strlen(str2);i++){
        final[j]=str2[i];
        j++;
    }
    printf("%s",final);
}