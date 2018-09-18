#include<stdio.h>
#include<graphics.h>

void makeCircle(int,int,int);
void main()
{
int gd=DETECT,gm,error,x,y,r;
initgraph(&gd,&gm,"");

makeCircle(100,50,50);
closegraph();

}
void makeCircle(int x0,int y0,int r)
{
int x=r;
int y=0;
int err=0;
while(x>y)
  {
   putpixel(x0+x,y0+y,7);
   putpixel(x0+y,y0+x,7);
   putpixel(x0+x,y0-y,7);
   putpixel(x0+y,y0-x,7);
   putpixel(x0-y,y0-x,7);
   putpixel(x0-x,y0-y,7);
   putpixel(x0-x,y0+y,7);
   putpixel(x0-y,y0+x,7);
   if(err<=0)
     {
      y=y+1;
      err=err+(2*y)+1;
     }
   else if(err>0)
     {
      x=x-1;
      err=err-(2*x)+1;
     }
   
  }
delay(10000);
closegraph();
}
