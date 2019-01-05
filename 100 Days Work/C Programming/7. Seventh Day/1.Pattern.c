Enter the value of n:10                                                                                                        

**********                                                                                                                     
*        *                                                                                                                     
*        *                                                                                                                     
*        *                                                                                                                     
*        *                                                                                                                     
*        *                                                                                                                     
*        *                                                                                                                     
*        *                                                                                                                     
*        *                                                                                                                     
**********   



#include<stdio.h>
void main()
{
    int i,j,k,n;
    printf("Enter the value of n:");
    scanf("%d",&n);
   for(i=1;i<=n;i++){
      for(j=1;j<=n;j++){
       if(i>=2 && j>=2 && j<n && i<n){
       printf(" ");}
       else{
           printf("*");
       }
      }  
       printf("\n");
   }
}
