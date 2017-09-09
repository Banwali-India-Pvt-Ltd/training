// The program checks if the character is upper case or not
// class to create an object
public class IsUpperMethod 
{
	// main method to create program
	public static void main(String[] args)
	{
		char a = 'Z';
		char b = 'a';
		
		System.out.println(Character.isUpperCase(a));       // True
		System.out.println(Character.isUpperCase(b));       // False
		System.out.println(Character.isUpperCase('A'));     // True
		System.out.println(Character.isUpperCase('z'));     // False
	}

}
