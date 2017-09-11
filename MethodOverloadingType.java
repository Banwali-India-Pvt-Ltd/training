// The program returns value with methodoverloading by same method
// class to create an object
public class MethodOverloadingType
{
	//main method to create program
	public static void main(String[] args)
	{
		MethodOverloadingType obj = new MethodOverloadingType();   // create an object
		obj.disp(5, 11.7);       // define value to call
		obj.disp(10, 14);        // define value to call
	}
	void disp(int a, int b)           // instance method
	{
		int x = a; 
		int y = b;	
		int z = x+y;                 // store total of a&b in the z 
		System.out.println(z);       // print or display z
	}
	void disp(int a, double b)         // instance method
	{
		int x = a; 
		double y = b;
		double z = x*y;              // store multiplication of a&b in the z
		System.out.println(z);       // display or print z 
	}

}
