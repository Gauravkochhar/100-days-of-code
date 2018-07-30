/*    
Puzzle-        How many minimum attempts to find the heaviest ball from the bag in which there are some balls . 
Condition:-    (if only two balls can be throw in a single attempt.)
*/


#include<stdio.h>
#include<conio.h>
static int atmpt=0;
void Attempt1(int hf,int w[],int sum,int sum1)
{
int hff,i,summ=0,summ1=0;
hff=hf/2;

    if(sum>sum1)
    {
	for(i=1;i<=hff;i++)
	{
	summ=summ+w[i];
	}
	atmpt+=1;
	 if(hff>1)
	{
	Attempt1(hff,w,summ,summ1);
	}
	else
	{
	printf("\n*********************************************************\n");
	printf("Total Minimum number of Attempts are:%d",atmpt);
	}
    }
    else
    {
	for(i=hff+1;i<=hf;i++)
	{
	summ1=summ1+w[i];
	}
	atmpt+=1;
	 if(hff>1)
	{
	Attempt1(hff,w,summ,summ1);
	}
	else
	{
	printf("\n*********************************************************\n");
	printf("Total Minimum number of Attempts are:%d",atmpt);
	}
    }

}
void Attempt(int w[],int no)
{
int i,sum=0,sum1=0,hf;
	printf("\n*********************************************************\n");
printf("Weight of the balls are: ");

    for(i=1;i<=no;i++)
    {
	if(i!=no)
	{
	printf("%d,",w[i]);
	}
	else
	{
	printf("%d",w[i]);
	}
    }
	printf("\n*********************************************************\n");
hf=no/2;
atmpt+=1;
for(i=1;i<=hf;i++)
{
sum=sum+w[i];
}
printf("\n\nWeight of starting %d th balls is=%d\n",hf,sum);
for(i=hf+1;i<=no;i++)
{
sum1=sum1+w[i];
}
printf("Weight of Last %d balls is=%d\n",hf,sum1);
Attempt1(hf,w,sum,sum1);
}
void main()
{
int i,w[20],no;
clrscr();
printf("Enter the number of balls:");
scanf("%d",&no);
for(i=1;i<=no;i++)
{
printf("\n %d th ball's weight is: ",i);
scanf("%d",&w[i]);
}
Attempt(w,no);
getch();
}
