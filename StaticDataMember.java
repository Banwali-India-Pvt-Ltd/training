/* The program runs all types variable besides Instance variable
 * Because of it is a static method and a static method can not use 
 * non static data member but it can access local and static variables 
 * Not any Instance variables
 */
// class to create an object
public class StaticDataMember
{
	int a = 10;         // Instance method 
	static int b = 20;  // Static variable
	
	
	// main method to create program
	public static void main(String[] args)
	{
		int x = 30;    // local variable
		
		System.out.println("local variable x " + x);    // display local variable value
		
		System.out.println("static variable b " + b);   // display static variable value
		
		// System.out.println("instance variable a " + a); won't run & it will show error
		
	}

}
