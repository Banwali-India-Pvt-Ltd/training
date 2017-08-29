// The program get number&input from user
// import to get input & define Scanner class
import java.util.*;
// class to create object
public class GetInputIn2DwithNumber {
	// main method to create program
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		// m,n to hold the values
		System.out.println("Input rows");
		int m = sc.nextInt();
		System.out.println("Input columns");
		int n = sc.nextInt();
		
		int [][] num = new int[m][n];
		// two loop to store the values
		for(int i=0; i<m; i++)
		{
			for(int j=0; j<n; j++)
			{
				num[i][j] = sc.nextInt();
			}
		}
		// two loop to display the values
		for(int i=0; i<m; i++)
		{
			for(int j=0; j<n; j++)
			{
				System.out.println(num[i][j]);
			}
		}
		// in the end of close Scanner class
		sc.close();
		
		
	}

}
