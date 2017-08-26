/* The program is based on Nested loop 
 * which print value from the inner loop 
 */
// The class use to make program where first letter of class in the capital
public class NestedLoop {
	// after using the class need to write the main method
	public static void main(String[] args){
		// Now need to define value in Outer & Inner loop
		for(int i=1; i<=5; i++)
		{
			for(int j=1; j<=4; j++)
			{
				System.out.print(i);
			}
			// In the outer loop println to leave current line
			System.out.println("");
		}
	}

}
