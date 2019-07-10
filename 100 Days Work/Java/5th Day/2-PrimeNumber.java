Enter number in series:                                                                                                        
10                                                                                                                             
2, 3, 5, 7, 11, 13, 17, 19, 23, 29,  


import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int i=0,j=0,temp=0;
		System.out.println("Enter Total prime number you want from 0 to infinity");
		int totalPrime = in.nextInt();
		int count = 0;
		int n = Integer.MAX_VALUE;
		for(i = 1 ; i <= n; i++){
		    if(temp == totalPrime){
		        break;
		    }
		    count = 0;
		    for(j=1;j<=i;j++){
		        if(i%j == 0){
		            count = count + 1;
		        }
		    }
		    if(count == 2){
		            System.out.print(i+", ");
		            temp = temp+1;
		    }
		}
	}
	
	
}
