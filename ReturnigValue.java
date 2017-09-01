// The program execute return value
// class to create method
public class ReturnigValue 
{
	// main method to create program
	public static void main(String[] args)
	{
		Test sc = new Test();
		System.out.println("Addition = " + sc.add());  // Addition
		
		int r = sc.mult(5);
		System.out.println("Multiplication = " + r);  // Multiplication 
	}
}
class Test
{
	int add()    // Instance method without parameter
	{
		int a = 10, b = 20;  // local variable
		return(a+b);
	}
	int mult(int p)   // instance method with parameter
	{
		int k = p; // local variable
		return(k*k);
		
	}
}
