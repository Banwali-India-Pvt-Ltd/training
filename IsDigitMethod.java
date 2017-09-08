// The program checks if the value is Number or not
// class to create an object
public class IsDigitMethod 
{
	// main method to create program
	public static void main(String[] args)
	{
		char a = 'Z';
		char b = '1';
		
		System.out.println(Character.isDigit(a));         // false
		System.out.println(Character.isDigit(b));         // true
		System.out.println(Character.isDigit('A'));       // false
		System.out.println(Character.isDigit('1'));       // true
		System.out.println(Character.isDigit('&'));       // false
	}

}
