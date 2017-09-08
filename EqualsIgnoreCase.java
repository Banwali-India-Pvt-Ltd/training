// The program compares two strings and ignores letters ( upper or lower )
// class to create object
public class EqualsIgnoreCase
{
	// main method to create program
	public static void main(String[] args)
	{
		String str1 = "Banwali";
		String str2 = "BANWALI";
		String str3 = "UFT";
		
		System.out.println(str1.equalsIgnoreCase(str2));  // True
		System.out.println(str2.equalsIgnoreCase(str3));  // False
	}

}
