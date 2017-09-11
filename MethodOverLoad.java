// The program return values on based on method overload
// class to create an object
public class MethodOverLoad 
{
	// main method to create program
public static void main(String[] args)
{
	
	MethodOverLoad obj = new MethodOverLoad();  // create an object to call to store values
	
	obj.test1();                       // store all values with class name & assign values
	obj.test2(10);
	obj.test3(10,20);
	obj.test4(123.45);
	
}
public void test1()                // create class without parameters
{
	System.out.println("No parameters");
}
public void test2(int a)           // create class with one parameter
{
	System.out.println("a = "+ a);
}
public void test3(int a, int b)    // create class with two parameters
{
	System.out.println("a & b = "+ a +" " + b);
}
public void test4(double a)        // create class with one parameter double
{
	System.out.println("double a = " + a*a);
	
}
}
