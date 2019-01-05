Enter the size of the pattern: 6                                                                                                 
     *                                                                                                                           
    ***                                                                                                                          
   *****                                                                                                                         
  *******                                                                                                                        
 *********                                                                                                                       
***********                                                                                                                      
 *********                                                                                                                       
  *******                                                                                                                        
   *****                                                                                                                         
    ***                                                                                                                          
     *          


#include<stdio.h>
void main(){
    int i,j,k,l,n;
    printf("Enter the size of the pattern: ");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        for(j=n;j>i;j--){
            printf(" ");
        }
        for(k=1;k<(2*i);k++){
            printf("*");
        }
        printf("\n");
    }
    for(i=n-1;i>=1;i--){
        for(j=n-1;j>=i;j--){
            printf(" ");
        }
        for(k=1;k<(2*i);k++){
            printf("*");
        }
        printf("\n");
    }
}
