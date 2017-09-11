// The program returns the value which is based on methodoverloading
// class to create an object
public class MethOverNumber 
{
	// main method to create program
	public static void main(String[] args)
	{
		MethOverNumber obj = new MethOverNumber();      // create an object
		obj.disp(10);                                   // disp first method
		obj.disp(10,20);                                // disp second method
	}
	void disp(int a)                              // Instance method
	{
		int x = a;                           // store value of a in x
		System.out.println("Value of a " + x);     // display x
	}
	void disp(int a, int b)                      // Instance method
	{
		int x = a;                               // store value of a & b in x & y
		int y = b;
		int z = x*y;                            // * both value which stored in x,y
		System.out.println("Multiplication of x & y= " +z);                  // display z 
	}
	

}
