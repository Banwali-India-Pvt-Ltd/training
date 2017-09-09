// The program prints an array using for loop one by one
// class to create an object
public class AnArrayLoop 
{
	// main method to create program
	public static void main(String[] args)
	{
		String[] array1 = {"Banwali", "LFT", "RFT", "SlikTest", "LoadRunner"};
		int [] array2 = { 10,20,30,40};
		
		for(int i=0; i<array1.length; i++)
		{
			System.out.println(array1[i]);    // prints array1 list one by one
		}
		for(int j=0; j<array2.length; j++)
		{
			System.out.println(array2[j]);   // prints array2 list one by one
		}
	}

}
