// The program checks & compare the string similar or not
// class to create method 
public class EqualsIgnoreMethod 
{
	// main method to create program
public static void main(String[] args)
{
	String str1 = " selenium ";
	String str2 = " UFT ";
	String str3 = " SELENIUM ";
	String str4 = " SELENIUM ";
	
	System.out.println(str3.equalsIgnoreCase(str4));   // returns true
	
	System.out.println(str1.equalsIgnoreCase(str3));   // returns true
	
	System.out.println(str1.equalsIgnoreCase(str2));   // returns false
	
}
}
