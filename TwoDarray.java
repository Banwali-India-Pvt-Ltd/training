// Import is a package to define Scanner class
import java.util.*;
/* TwoDarray is a class and the file name & class name always will be same. 
 * The first letter of class always will be in the capital
 */
public class TwoDarray {
	/* Main is a method.
	 * String is a pre-defined class
	 */
public static void main(String[] args){
	// Scanner is a class to get input from user
	Scanner sc = new Scanner(System.in);
	// int marks to assign arrays
	int[] [] marks = new int[5] [4];
	// run loops in the limit of arrays
	for(int i=0; i<5; i++){
		for(int j=0; j<4; j++){
			// send i&j variable in the Scanner next method
			marks[i] [j] = sc.nextInt();
			
		}
		
		
		
	}
	// Again for loop to print same number after input
	for(int k=0; k<5; k++){
		for(int p=0; p<4; p++){
			System.out.println(marks[k][p]);
		}
	}
	// close the Scanner class after completing the program
	sc.close();
	
}
}
