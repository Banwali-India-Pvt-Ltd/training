// The program checks whether the value Alfa byte or not
// class to create method
public class CharIsMethod
{
	public static void main(String[] args)
	{
		char a = '1';
		
		System.out.println(Character.isLetter(a)); // return false
		System.out.println(Character.isLetter('A')); // returns true
		System.out.println(Character.isLetter('a')); // returns true
		System.out.println(Character.isLetter('*')); // returns false
	}

}
