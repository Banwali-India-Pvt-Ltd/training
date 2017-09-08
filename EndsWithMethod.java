/* The program checks if the string ends with specified suffix or not
 * And supports 2-way comparison 
 */
// class to create object
public class EndsWithMethod
{
	// main method to create program
	public static void main(String[] args)
	{
		String str = "Welcome to the Banwali Company";
		
		System.out.println(str.endsWith("Banwali Company"));  // True
		System.out.println(str.endsWith("Company"));          // True
		System.out.println(str.endsWith("Banwali"));          // False
		System.out.println(str.endsWith("Banali Company"));   // False
	}

}
