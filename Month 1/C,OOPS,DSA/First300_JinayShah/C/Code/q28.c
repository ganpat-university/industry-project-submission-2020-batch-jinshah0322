#include<stdio.h>
#include<string.h>
#include <ctype.h>
void main(){
    char str[100];
    int consonant=0,vowels=0;
    scanf("%s",&str);
    for(int i=0;i<strlen(str);i++){
        if(tolower(str[i])!='a' && tolower(str[i])!='e' && tolower(str[i])!='i' && tolower(str[i])!='o' && tolower(str[i])!='u'){
            consonant++;
        } else{
            vowels++;
        }
    }
    printf("Consonants=%d and vowels=%d",consonant,vowels);
}   