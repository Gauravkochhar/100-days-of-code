input

3 5
13 4 8 14 1
9 6 3 7 21
5 12 17 9 3


output

13 9 5
4 6 12
8 3 17
14 7 9
1 21 3




import java.util.*;
class TestClass {
    public static void main(String args[] ) throws Exception {
        Scanner in = new Scanner(System.in);
        int row= in.nextInt();
        int column= in.nextInt();
        int result[][]=new int[row][column];
        int resultFinal[][]= new int[column][row];
        int i,j;
        for(i=0;i<row;i++){
            for(j=0;j<column;j++){
                result[i][j]= in.nextInt();
                resultFinal[j][i]= result[i][j];        
            }
        }
        for(i=0;i<column;i++){
            for(j=0;j<row;j++){
                System.out.print(resultFinal[i][j]+" ");
            }
            System.out.print("\n");
        }
    }
}





