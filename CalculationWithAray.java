// The program calculate values with arrays
// class name with first letter of capital
public class CalculationWithAray {
	// main method to implement program
	public static void main(String[] args)
	{
		int [] num = new int[5];
		// define the value to calculate
		num[0] = 11;
		num[1] = 22;
		num[2] = num[0] + num[1];
		num[3] = num[1] + 10;
		num[4] = num[0];
		// run Loop instead of write whole things
	for(int i=0; i<5; i++)
	{
		System.out.println(num[i]);
	}
	}

}
