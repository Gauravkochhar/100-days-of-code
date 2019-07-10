Enter number of series:                                                                                                        
5                                                                                                                              
1, 1, 2, 3, 5, 


import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		System.out.println("Enter number of series: ");
		int n = in.nextInt();
		int[] fibSeries = getFibonacci(n);
		System.out.println("\n");
		for(int i=0;i<fibSeries.length;i++){
		    System.out.print(fibSeries[i]+", ");
		}
	}
	
	public static int[] getFibonacci(int n){
	    int i=0,j=0,sum=0,num1=0,num2=0;
	    int[] fibSeries = new int[n];
	    
	    for(i=1;i<n-1;i++){
		    if(i==1){
		        num1 = 1;
		        num2 = 1;
		        sum = num1 + num2;
		        System.out.print(num1+", "+num2+ ", "+sum+", ");
		        fibSeries[0]=1;
	            fibSeries[1]=1;
	            fibSeries[2]=2;
		    }
		    else{
		        num2 = num1;
		        num1 = sum;
		        sum = num1 + num2;
		        System.out.print(sum + ", ");
		        fibSeries[i+1] = sum;
		    }
		}
		return fibSeries;
	}
}
