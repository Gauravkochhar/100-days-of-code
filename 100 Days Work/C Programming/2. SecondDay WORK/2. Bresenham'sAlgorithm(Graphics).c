#include<stdio.h>
#include<conio.h>
#include<graphics.h>
void breline(int,int,int,int);
void main()
{
int gd=DETECT,gm;
int x1,y1,xn,yn;
initgraph(&gd,&gm,"");
printf("Enter the first coardinate:");
scanf("%d%d",&x1,&y1);
printf("Enter the ending coardinate:");
scanf("%d%d",&xn,&yn);
breline(x1,y1,xn,yn);
getch();
closegraph();
}
void breline(int x1,int y1,int xn,int yn)
{
int dx,dy,di,dp,dn;
dx=xn-x1;
dy=yn-y1;
di=2*dy-dx;
dp=2*dy-2*dx;
dn=2*dy;

putpixel(x1,y1,RED);
while(x1<xn)
{
    x1++;
    if(di<0)
    {
      di=di+dn;
    }
    else
    {
      y1++;
      di=di+dp;
    }
    putpixel(x1,y1,RED);
    delay(5);
}

}
