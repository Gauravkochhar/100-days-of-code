Enter the size of n:3                                                                                                          

*                                                                                                                                
***                                                                                                                              
*                                                                                                                                
*                                                                                                                                
*****                                                                                                                            
*                                                                                                                                
*                                                                                                                                
*                                                                                                                                
*******                                                                                                                          
  


#include<stdio.h>
#include<conio.h>
void fun(int n,int c){
int i,j,k;
for(i=1;i<=n;i++){
printf("*\n");
}
for(k=1;k<=c;k++){
printf("*");
}
printf("\n");
}

void main()
{
int i,j,k,n;
static int c=1;
clrscr();
printf("Enter the size of n:");
scanf("%d",&n);
for(i=1;i<=n;i++){
c=c+2;
fun(i,c);

}
getch();
}
