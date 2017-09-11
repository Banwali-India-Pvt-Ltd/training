// The program return the value on the base of Nesting static/static in the static
// class to create an object
public class NestingStaticMethod
{
	// main method to create program
	public static void main(String[] args)
	{
		disp();          // another method name has to be call
	}
	public static void disp()           // create another static method with name of disp
	{
		int x = 10;                     // local variables
		int y = 30;
		int z = x*y;                    // Multiply x y & stored in z
		System.out.println("Value of z = " + z);       // display z 
	}

}
