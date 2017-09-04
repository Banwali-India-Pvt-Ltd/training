// The program checks weather the value number or not
// class to create method
public class CharIsDigit 
{
	// main method to create program
	public static void main(String[] args)
	{
		char a = '1';
		System.out.println(Character.isDigit(a)); // returns true
		System.out.println(Character.isDigit('A')); // returns false
		System.out.println(Character.isDigit('a')); // returns false
		System.out.println(Character.isDigit('*')); // returns false
		System.out.println(Character.isDigit('7')); // returns true
	}

}
