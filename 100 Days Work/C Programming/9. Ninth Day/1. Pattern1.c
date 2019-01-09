Enter the number of size of the pattern:5       

                    (((((*)))))                                                                                                  
            ((((*))))                                                                                                            
      (((*)))                                                                                                                    
  ((*))                                                                                                                          
(*) 
 
 
 #include<stdio.h>
 #include<conio.h>

 void fun(int n){
 int i,j,k;
 for(i=1;i<=n*(n-1);i++){
 printf(" ");
 }
 for(i=1;i<=n;i++){
 printf("(");
 }
 if(n>0){
 printf("*");}
 for(i=1;i<=n;i++){
 printf(")");
 }
 printf("\n");
 }
 void main()
 {
 int i,j,k,n;
 clrscr();
 printf("Enter the number of size of the pattern:");
 scanf("%d",&n);
 for(i=n;i>=1;i--){
   fun(i);
 }
 getch();
 }
