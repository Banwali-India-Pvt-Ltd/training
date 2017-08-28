// The array gets input from user
// Import to define Scanner class
import java.util.*;
// defined class with first capital letter
public class GetInputArray {
	// using main method to implement program
	public static void main(String[] args)
	{
		// Using Scanner class to get input
	Scanner sc = new Scanner(System.in);
	int [] num = new int[5];
	// using For Loop to store value
	for(int i=0; i<5; i++)
	{
		num[i] = sc.nextInt();
	}
	// using For Loop to display values
	for(int i=0; i<5; i++)
	{
		System.out.println(num[i]);
	}
	sc.close();
	}
	

}
