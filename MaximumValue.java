// The program returns maximum values between two numbers

// class to create method
public class MaximumValue
{
	// main method to create program
	public static void main(String[] args)
	{
		int a = 10, b = 20;
		double c = 1.234, d = 3.567;
		
		System.out.println(Math.max(a, b)); // 20
		System.out.println(Math.max(c, d)); // 3.567
		System.out.println(Math.max(123, 124)); // 124
		System.out.println(Math.max(10.345, 10.3451)); // 10.3451
		System.out.println(Math.max(1, 1));  // 1
	}

}