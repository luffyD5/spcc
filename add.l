%{
#include <stdio.h>
%}

%option noyywrap

%%
[0-9]+      { printf("Number: %s\n", yytext); }
[ \t\n]     ; // Ignore whitespace characters
.           ; // Ignore any other character

%%

int main() {
    int num1, num2;
    printf("Enter the first number: ");
    scanf("%d", &num1);
    printf("Enter the second number: ");
    scanf("%d", &num2);
    printf("Sum: %d\n", num1 + num2);
    return 0;
}