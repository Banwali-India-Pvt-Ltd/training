// The program takes value from user
// define import to create Scanner class
import java.util.*;
// define class to create object
public class DynamicMemory {
	// define main method to implement program
	public static void main(String[] args)
	{
		// Scanner class to get input
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int [] num = new int[n];
		// Loop to store values
		for(int i=0; i<n; i++)
		{
			num[i] = sc.nextInt();
		}
		// Loop to display value
		for(int i=0; i<n; i++)
		{
			System.out.println(num[i]);
		}
		sc.close();
		
	}

}
