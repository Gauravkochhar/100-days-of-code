Enter number of series:8                                                                                                         
0 1 1 2 3 5 8 13 21                                                                                                              
*                                                                                                                                
*                                                                                                                                
**                                                                                                                               
***                                                                                                                              
*****                                                                                                                            
********                                                                                                                         
*************                                                                                                                    
*********************  



import java.util.*;
public class Main
{
    
    
	public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int n=0;
        System.out.print("Enter number of series:");
        n= in.nextInt();
        int first=0;
        System.out.print(first+" ");
        int second=1;
        System.out.print(second+" ");
        int sum=0;
        List<Integer> ls=new ArrayList();
        ls.add(0);
        ls.add(1);
        sum=first+second;
        for(int i=1;i<n;i++){
            sum=first+second;
            first=second;
            second=sum;
            ls.add(sum);
            System.out.print(sum+" ");
        }
        int i=0;
	int j=0;
	    for(i=0;i<ls.size();i++){
	        for(j=0;j<ls.get(i);j++){
	            System.out.print("*");
	        }
	        System.out.println("");
	    }	
	}
}
