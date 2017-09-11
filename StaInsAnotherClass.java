// The program calls static method in Instance method in another class
// class to create an object
public class StaInsAnotherClass
{
	
	// main method to create program
	public static void main(String[] args)
	{
		Amar obj = new Amar();     // create an object with new class name
		obj.disp();                // because disp method have in another class
	}
	public static int add()        // create static method with name of add
	{
		int x = 10;                // local variables
		int y = 20;
		int z = x+y;               // store x,y values in z
		return z;                  // return value which have in z
	}

	
}
class Amar
{
	public void disp()
	{
		int a=StaInsAnotherClass.add();
		System.out.println("Addition ="+a);
	}
}