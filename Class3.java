// The program checks the method & returns the value
// class to create object
public class Class3 
{
	public int sub()
	{
		int a = 100, b = 45;
		int result = a-b;
		return result;
	}
	// main method to create program
	public static void main(String[] args)
	{
		Class3 obj = new Class3();
		int y = obj.sub();
		System.out.println(y);
	}
}
