#include<stdio.h>
#include<conio.h>
int* fun1(int *arr)
{

return arr;
}
void main()
{
int i,n,array[50];
int *d;
clrscr();
printf("Enter the number of element:");
scanf(" %d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&array[i]);
}
printf("Array you entered is:\n");
for(i=0;i<n;i++)
{
printf("%d\t",array[i]);
}
d=fun1(array);
printf("\nArray elements from the function are:\n");
for(i=0;i<n;i++)
{
printf("%d\t",*(d+i));
}
getch();
}
