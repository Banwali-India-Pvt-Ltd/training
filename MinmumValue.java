// The program returns minimum numbers between the two numbers
// class to create method
public class MinmumValue 
{
	// main method to create program
	public static void main(String[] args)
	{
		int a = 10, b = 20;
		double c = 1.234, d = 3.567;
		
		System.out.println(Math.min(a, b));  // 10
		System.out.println(Math.min(c, d));  // 1.234
		System.out.println(Math.min(123, 124));  // 123
		System.out.println(Math.min(10.345, 10.3451));  // 10.345
		System.out.println(Math.min(1,1));  // 1
	}

}
