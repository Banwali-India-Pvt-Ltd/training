// The program returns the maximum value between two numbers
// class to create object
public class MaxMethod 
{
	// main method to create program
	public static void main(String[] args)
	{
		int a = 5;
		int b = 7;
		
		double c = 10.234;
		double d = 10.794;
		
		System.out.println(Math.max(a, b));        // 7
		System.out.println(Math.max(c, d));        // 10.794
		System.out.println(Math.max(10, 17));      // 17
		System.out.println(Math.max(1.34, 2.3));   // 2.3
	}

}
