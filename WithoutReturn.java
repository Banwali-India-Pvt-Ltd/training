/* The problem in this program what is the sense of use return value 
 * does the print statement not returns value 
 * Why used main function below side & if upper side than 
 * Why required to write syso together main method ?
 */
public class WithoutReturn {
// Create a static method with return value and no parameters
	public static int multiply()
	{
		int a = 10, b = 20;
		int result = a*b;
		return result;
		
	}
	public static void main(String[] args)
	{
		int res = WithoutReturn.multiply();
		System.out.println(res);
	}
}
