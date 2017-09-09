// The program returns if an Array contains certain value or not
// import to write predefine method arrays
import java.util.Arrays;
// class to create an object
public class ArrayContains 
{
	// main method to create program
	public static void main(String[] args)
	{
		String[] array1 = { "Banwali", "UFT", "RFT", "SlikTest", "LoadRunner"};
		
		boolean b = Arrays.asList(array1).contains("UFT");
		
		boolean c = Arrays.asList(array1).contains("Banwali");
		
		boolean d = Arrays.asList(array1).contains("Java");
		System.out.println(b);      // true
		System.out.println(c);      // true
		System.out.println(d);      // false
	}

}
