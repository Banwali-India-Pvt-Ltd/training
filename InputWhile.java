/* The program is related to while loop
 * it works until the loop doesn't false
 * we can put any condition here to exit the program
 */
// import package to define Scanner class
import java.util.Scanner;
// The class with first name of capital
public class InputWhile {
	public static void main(String[] args){
		// Scanner class to get input
		Scanner sc = new Scanner(System.in);
		int i;
		while(true)
		{
			System.out.println("Enter any integer value");
			
			i = sc.nextInt();
			if(i==0)
			{
				break;
			}
			System.out.println(i);
		}
		sc.close();
	}

}
