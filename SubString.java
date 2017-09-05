// The program returns sub string from string
// class to create method
public class SubString 
{
	// main method to create program
	public static void main(String[] args)
	{
		String str1 = " Welcome to Banwali Company ";
		
		System.out.println(str1.substring(11));  // returns Banwali Company
		
		System.out.println(str1.substring(19));  // returns Company
		
		System.out.println(str1.substring(11,19));   // returns Banwali
	}

}
