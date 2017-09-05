// The program compare to string 
// class to create method
public class CompareToString
{
	// main method to create program
public static void main(String[] args)
{
	String str1 ="SELENIUM";
	String str2 ="selenium";
	String str3 ="seleniuma";
	String str4 ="selenium";
	int result;
	result = str1.compareTo(str2);
	System.out.println(result); //
	 
	result = str3.compareTo(str2);
	System.out.println(result); //
	 
	result = str2.compareTo(str4);
	System.out.println(result); //
}
}
