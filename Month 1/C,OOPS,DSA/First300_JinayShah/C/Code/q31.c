#include<stdio.h>
#include<string.h>
void main(){
    char str1[100],str2[100], chTemp;
    scanf("%s %s",&str1,&str2);
    for(int i=0; i<strlen(str1); i++)
    {
        for(int j=0; j<(strlen(str1)-1); j++)
        {
            if(str1[j]>str1[j+1])
            {
                chTemp = str1[j];
                str1[j] = str1[j+1];
                str1[j+1] = chTemp;
            }
        }
    }
    for(int i=0; i<strlen(str2); i++)
    {
        for(int j=0; j<(strlen(str2)-1); j++)
        {
            if(str2[j]>str2[j+1])
            {
                chTemp = str2[j];
                str2[j] = str2[j+1];
                str2[j+1] = chTemp;
            }
        }
    }
    if(!(strcmp(str1,str2))){
        printf("anagram");
    } else{
        printf("not anagram");
    }
}