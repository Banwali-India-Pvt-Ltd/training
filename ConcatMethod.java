// The program returns String concatenation
// class to create method
public class ConcatMethod
{
	// main method to create program
public static void main(String[] args){
	String str1 ="Selenium";
	String str2 = " Java";
	String str3 = " sam ";
	str1 = str1.concat(str3);
	str1 = str1.concat(str2);
	System.out.println(str1);   // returns Selenium sam Java
	
}
}
