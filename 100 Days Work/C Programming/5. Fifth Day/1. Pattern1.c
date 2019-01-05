*     *                                                                                                                        
 *   *                                                                                                                         
  * *                                                                                                                          
   *       

 

#include<stdio.h>
void main()
{
    int i,j,k,l;
    printf("Enter the value of the pattern size :");
    scanf("%d",&l);
    for(i=4;i>=1;i--){
        for(j=4;j>i;j--){
            printf(" ");
        }
        for(k=1;k<(2*i);k++){
            if(k>1 && k<(2*i)-1){
              printf(" ");  
            }
            else{
               printf("*"); 
            }
            
        }
        printf("\n");
    }
    
}
