#include<stdio.h>
#include<conio.h>
void bubble_sort(int A[],int N);
int main()
{
int i,n;
clrscr();
int A[]={29,34,15,8};
for(i=0;i<4;i++){
scanf("%d \t",&A[i]);
}
bubble_sort(A,4);
 getch();
return 0;
}
void bubble_sort(int A[],int N)
{
int temp;
int i,round;
for(round=1;round<=N-1;round++)
   {
      for(i=0;i<=N-1-round;i++)
      {
	if(A[i]>A[i+1])
	{
	temp=A[i+1];
	A[i+1]=A[i];
	A[i]=temp;
	}
      }
    }
    for(i=0;i<N;i++)
    {
    printf("%d \n",A[i]);
    }
}
