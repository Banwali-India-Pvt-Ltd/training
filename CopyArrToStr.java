// The program copy array to string an print an array
// import package to use predefine arrays class
import java.util.Arrays;
// class to create an object
public class CopyArrToStr 
{
	// main method to create program
	public static void main(String[] args)
	{
		String Array[] = {"Banwali", "UFT", "RFT", "SlikTest", "LoadRunner"};
		String str = Arrays.toString(Array);
		
		System.out.println(str);
	}

}
