    *                                                                                                                          
   * *                                                                                                                         
  *   *                                                                                                                        
 *     * 



#include <stdio.h>
int main()
{
    int i,j,k,h;
   for(i=1;i<=4;i++){
       for(j=4;j>=i;j--){
           printf(" ");
       }
      /* for(k=1;k<=i;k++){
           printf("*");
       }
       for(h=2;h<=i;h++){
           printf("*");
       }*/
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

    return 0;
}
