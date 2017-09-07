/* The program returns sum of the numbers  
 * And the class uses to extends to another class
 */
// class to create method
public class Class1 {
public int add(int a, int b)
{
	int result = a+b;
	return result;
}
// main method to create object
public static void main(String[] args)
{
	Class1 obj1 = new Class1();
	int res = obj1.add(10,20);
	System.out.println(res);
}
}

	

