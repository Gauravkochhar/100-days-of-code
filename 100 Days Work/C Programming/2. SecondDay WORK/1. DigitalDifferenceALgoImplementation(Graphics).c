#include<stdio.h>
#include<conio.h>
#include<graphics.h>
void ddaline(int,int,int,int);
void main()
{
int gd= DETECT,gm;
int x1,y1,xn,yn;
initgraph(&gd,&gm,"");
printf("Enter first Coardinate:");
scanf("%d%d",&x1,&y1);
printf("Enter the ending Coardinate:");
scanf("%d%d",&xn,&yn);
ddaline(x1,y1,xn,yn);
getch();
closegraph();
}
void ddaline(int x1,int y1,int xn,int yn){
int m,dx,dy,i;
m=(yn-y1)/(xn-x1);
for(i=x1;i<xn;i++){
if(m<=1)
{
dx=1;
dy=m*dx;
}
else
{
dy=1;
dx=dy/m;
}
x1=x1+dx;
y1=y1+dy;
putpixel(x1,y1,RED);
delay(5);
}
}
