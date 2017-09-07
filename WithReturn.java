/* The same problem occuring in this program why requires to write main method 
 * below and if yes than why should we use syso together of this one 
 * Can I have any good understanding example for this logic
 */
public class WithReturn {
	
	// Create a static method with Return value and parameter
public static int multiply(int a , int b){
	int result = a*b;
	return result;
	}
public static void main(String[] args){
	int res = WithReturn.multiply(7, 9);
	System.out.println(res);

	
}
}
