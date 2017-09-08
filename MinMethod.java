// The program return the minimum value between the two numbers
// class to create object
public class MinMethod 
{
	// main method to create program
	public static void main(String[] args)
	{
		int a = 5;
		int b = 7;
		
		double c = 10.234;
		double d = 10.794;
		
		System.out.println(Math.min(a, b));             // 5
		System.out.println(Math.min(c, d));             // 10.234
		System.out.println(Math.min(10, 17));           // 10
		System.out.println(Math.min(12.34, 1.234));     // 1.234
	}

}
