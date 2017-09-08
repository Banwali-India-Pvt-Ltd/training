// The program checks if the value is Alpha byte or not
// class to create an object
public class IsLetterMethod 
{
	// main method to create program
	public static void main(String[] args)
	{
		char a = 'Z';
		char b = '1';
		
		System.out.println(Character.isLetter(a));       // True
		System.out.println(Character.isLetter(b));       // False
		System.out.println(Character.isLetter('A'));     // True
		System.out.println(Character.isLetter('7'));     // False
		System.out.println(Character.isLetter('*'));     // False
	}

}
