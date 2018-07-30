#include<stdio.h>
#include<conio.h>
#include<string.h>
void main()
{
int i,count=0;
char a[50],ch;
clrscr();
printf("Enter a string:");
gets(a);
for(ch='a';ch<='z';ch++)
{
count=0;
   for(i=0;i<=strlen(a);i++)
   {
	if(a[i]==ch)
	{
	count=count+1;
	}
   }
   if(count>0)
   {
   printf("%c comes %d times\n",ch,count);
   }
}
getch();
}
