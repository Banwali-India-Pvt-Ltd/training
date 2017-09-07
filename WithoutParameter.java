/* The same problem facing here why can I not write println statement 
 * in the non-static method without parameter
 * why it is requires to write in the main method ?
 */
public class WithoutParameter
{
public static void main(String[] args)
{
	// create object
	WithoutParameter obj = new WithoutParameter();
	// call method
	int x = obj.add();
	System.out.println(x);
}
// create a non-static method without parameter
public int add()
{
	int num1 = 10;
	int num2 = 20;
	int result = num1 + num2;
	return result;
	
}
}
