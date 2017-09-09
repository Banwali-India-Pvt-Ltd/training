import java.util.Arrays;

// The program creates an array and sort the array
// class to create an object
public class ArraySort 
{
	// main method to create program
	public static void main(String[] args)
	{
		int [] Nums = new int[6];
		
		Nums[0] = 14;
		Nums[1] = 10;
		Nums[2] = 36;
		Nums[3] = 55;
		Nums[4] = 78;
		Nums[5] = 37;
		
		Arrays.sort(Nums);
		
		for(int i=0; i<Nums.length; i++)
		{
			System.out.println(Nums[i]);
		}
	}

}
