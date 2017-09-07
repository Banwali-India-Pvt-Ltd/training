/* The problem is this program is that when I move main method
 * at upper side than why the system.out.println line showing error 
 * in the below side why requires to keep continue syso line with main method
 */

public class JavaMethod
{

// create a non-static method with parameter
	public int add1(int num1, int num2)
	{
		int result = num1+num2;
		return result;
	}
	public static void main(String[] args)
	{
		
		// create object
		JavaMethod obj = new JavaMethod();
		// call method
		int x = obj.add1(33, 20);
	    System.out.println(x);  // 53
	}
}