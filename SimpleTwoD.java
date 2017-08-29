// The program where we can define the value get print
// class to create object
public class SimpleTwoD {
	// main method to create program
	public static void main(String[] args)
	{
		// Declare the values in row and column
		int [][] num = new int [3] [4];
		num[0][0] = 11;
		num[0][1] = 22;
		num[0][2] = 33;
		num[0][3] = 44;
		num[1][0] = 55;
		num[1][1] = 66;
		num[1][2] = 77;
		num[1][3] = 88;
		num[2][0] = 10;
		num[2][1] = 20;
		num[2][2] = 30;
		num[2][3] = 40;
		
		System.out.println(num[0][1]); // print number which is 0&1 in
		System.out.println(num[1][2]); // print number which is 1&2 in
	}

}
