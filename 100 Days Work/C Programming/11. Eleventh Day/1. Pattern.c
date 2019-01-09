Enter the size of n:4                                                                                                            
 
   *                                                                                                                             
   ***                                                                                                                           
   *                                                                                                                             
   *                                                                                                                             
  *****                                                                                                                          
   *                                                                                                                             
   *                                                                                                                             
   *                                                                                                                             
 *******                                                                                                                         
   *                                                                                                                             
   *                                                                                                                             
   *                                                                                                                             
   *                                                                                                                             
********* 

#include<stdio.h>
#include<conio.h>
void fun(int max,int n,int c){
int i,j,k;
for(i=1;i<=n;i++){
for(j=1;j<=max-1;j++){
printf(" ");
}
printf("*\n");
}
if(max!=n){
for(j=1;j<=max-n;j++){
printf(" ");
}          }
for(k=1;k<=c;k++){

printf("*");
}


printf("\n");
}

void main()
{
int i,j,k,n,max;
static int c=1;
clrscr();
printf("Enter the size of n:");
scanf("%d",&n);
max=n;
for(i=1;i<=n;i++){
c=c+2;
fun(max,i,c);

}
getch();
}
