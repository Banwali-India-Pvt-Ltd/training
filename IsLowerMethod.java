// The program checks if the character is lower case or not
// class to create an object
public class IsLowerMethod 
{
	// main method to create program
	public static void main(String[] args)
	{
		char a = 'Z';
		char b = 'a';
		
		System.out.println(Character.isLowerCase(a));    // false
		System.out.println(Character.isLowerCase(b));    // true
		System.out.println(Character.isLowerCase('A'));  // false
		System.out.println(Character.isLowerCase('z'));  // true
		System.out.println(Character.isLowerCase('1'));  // false
	}

}
