// The program execute values in the nesting method
// class to create an object
public class NestingInstance
{
	// main method to create program
	public static void main(String[] args)
	{
		NestingInstance obj = new NestingInstance();
		obj.disp();
	}
	int add()                    // Instance method
	{
		int a = 10; int b = 20;
		int z = a+b;
		return z;
	}	
	
	
	void disp()                 // Instance method
	{
		int x = add();         // calling instance method, inside instance method
		System.out.println(x);
	}

}
