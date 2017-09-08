// The program compares two numbers and it supports 2 way comparison
// class to create object
public class EqualsNumberMethod
{
	// main method to create program
	public static void main(String[] args)
	{
		int a = 10;
		Integer b = Integer.valueOf(a);
		
		System.out.println(b.equals(Integer.valueOf(10)));   // true
		System.out.println(b.equals(Integer.valueOf(7)));    // false
		System.out.println(b.equals(Integer.valueOf(14)));   // false
	}

}
