#include<stdio.h>
void main(){
    float num1,num2,solution;
    char operator;
    scanf("%f %c %f",&num1,&operator,&num2);
    switch (operator)
    {
    case '+':
        solution=num1+num2;
        printf("%f",solution);
        break;

    case '-':
        solution=num1-num2;
        printf("%f",solution);
        break;

    case '*':
        solution=num1*num2;
        printf("%f",solution);
        break;

    case '/':
        solution=num1/num2;
        printf("%f",solution);
        break;
    
    default:
        break;
    }
}