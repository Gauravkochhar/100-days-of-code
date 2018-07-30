#include<stdio.h>
#include<conio.h>
int palin(int palin);
void main()
{
    int num,reverse;
    clrscr();
    printf("Enter a number to check palindrome or not:\n");
    scanf("%d",&num);
    reverse=
    palin(num);
    if(reverse==num)
    {
    printf("\nEntered Number is Palindrome.");
    }
    else
    {
    printf("\nNot Palindrome");
    }
    getch();
}
int palin(int num)
{
    int r=0;
    int rem;
    while(num>0)
    {
    rem=num%10;
    r=(r*10)+(rem);
    num=num/10;
    }
    return r;
}
