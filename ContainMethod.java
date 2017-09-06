import java.util.Arrays;


// The program checks the array contains certain value or not
// class to create method
public class ContainMethod 
{
	// main method to create program
	public static void main(String[] args)
	{
		String [] arr1 = {"UFT", "Banwali", "RFT", "Test"};
		
		boolean a = Arrays.asList(arr1).contains("UFT");
		boolean b = Arrays.asList(arr1).contains("uft");
		
		System.out.println(a);   // true
		System.out.println(b);   // false
	}

}
