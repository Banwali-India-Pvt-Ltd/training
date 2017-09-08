/* The program compare to string weather it is true or false
 * Why it is showing value of 32 while display ?
 */
// class to create object 
public class CompareToMethod 
{
	// main method to create program
	public static void main(String[] args)
	{
		String str1 = "selenium";
		String str2 = "SELENIUM";
		String str3 = "seleniuma";
		String str4 = "selenium";
		
		System.out.println(str1.compareTo(str2));  // positive value
		System.out.println(str1.compareTo(str3));  // negative value
		System.out.println(str1.compareTo(str4));  // 0
	}

}
