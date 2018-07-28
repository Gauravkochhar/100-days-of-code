#include<stdio.h>
#include<conio.h>
void binarySearch(int * a,int se,int n,int low,int high)
{
int i,mid;
mid=(low+high)/2;
if(a[mid]==se)
{
printf("************************************************************");
printf("\nSearch is successful,element exists at %dth Index.",mid);
printf("************************************************************");
return 1;
}
else if(se>a[mid])
{
low=mid+1;
binarySearch(a,se,n,low,high);
}
else if(se<a[mid])
{
high=mid-1;
binarySearch(a,se,n,low,high);
}
else
{
printf("************************************************************");	
printf("\nElement is not present in the list.");
printf("************************************************************");
}

}
void main()
{
int a[20],i,n,se,low=0,high;
clrscr();
printf("Enter the no. of elements in Array: \n");
scanf("%d",&n);
high=n;
printf("Enter elements in sort form\n");
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
printf("Elements are:");
for(i=0;i<n;i++)
{
	if(i==n-1)
	{
	printf("%d",a[i]);
	}
	else
	{
	printf("%d,",a[i]);
	}
}
printf("\nEnter the element you want to search: \n");
scanf("%d",&se);
binarySearch(a,se,n,low,high);
getch();
}
