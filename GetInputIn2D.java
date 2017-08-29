// In 2D get input from user
// Use import method to get input
import java.util.*;
// class to create object
public class GetInputIn2D {
	// main method to create program
	public static void main(String[] args)
	{
		// Scanner class for input
		Scanner sc = new Scanner(System.in);
		// Initialization the values
		int [] [] num = new int [3][4];
		// loop to create rows size
	for(int i=0; i<3; i++)
	{
		// loop to create columns size
		for(int j=0; j<4; j++)
		{
			// sc next method to store value
			num[i][j] = sc.nextInt(); 
		}
	}
	// Again loop to display the values
	for(int i=0; i<3; i++){
		for(int j=0; j<4; j++)
		{
			System.out.print(num[i][j] + " ");
		}
		// To leave the current line
		System.out.println("");
		
		
	}
	sc.close();
		
	}

}
