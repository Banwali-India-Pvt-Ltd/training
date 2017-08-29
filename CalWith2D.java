// The is used for calculation with 2D array
// class name to create object
public class CalWith2D {
	// main method to create program
	public static void main(String[] args){
		int[] [] num = new int [3] [4];
		
		num[0][0] = 11;
		num[0][1] = 22;
		num[0][2] = 33;
		num[0][3] = 44;
		num[1][0] = num[0][1] + num[0][2];
		num[1][1] = num[0][0] + 60;
		num[1][2] = 77;
		num[1][3] = 88;
		num[2][0] = 10;
		num[2][1] = 20;
		num[2][2] = 30;
		num[2][3] = 40;
		
		// Loop to print all values
		for(int i=0; i<3; i++){
			for(int j=0; j<4; j++){
				System.out.println(num[i][j]);
			}
		}
		
	}

}
