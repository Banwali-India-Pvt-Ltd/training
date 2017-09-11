// The program execute total of numbers in between two class
// class to create an object
public class NestingInsAnotherClass
{
	// main method to create program
	public static void main(String[] args)
	{
		NestingInsAnotherClass obj = new NestingInsAnotherClass();
		obj.disp();
	}
	void disp()
	{
		Test ob = new Test();        // create another object for new class
		int x = ob.add();            /* control transfer in add method
		                                which have in another class */
		System.out.println(x);
	}
}
class Test
{
	int add()
	{
		int a = 10; int b = 20;
		int z = a+b;
		return z;                 // return z value goes to in the disp method 
	}
}
