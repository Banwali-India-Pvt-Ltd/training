// The program calls static method in Instance method
// class to create an object
public class StamethodInInsMethod
{
	// main method to create program
	public static void main(String[] args)
	{
		StamethodInInsMethod obj = new StamethodInInsMethod();   // create an object 
		                                                         // to call disp method
		obj.disp();
	}
	public static int add()         // create static method with name of add
	{
		int x = 10;                 // local variables x, y
		int y = 20;
		int z = x+y;               // store value of x,y in z
		return z;                  // return z value which stored
	}
	public void disp()             // create disp method to call add method
	{
		int a = add();             // store value of add in a
		System.out.println("Addition = " + a);              // finally print a where stored value
		
	}
}
