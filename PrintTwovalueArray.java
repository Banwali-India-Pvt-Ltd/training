/* If we print here a[1] then
 * we will get 5 if a[0] then
 * we will get 4 if a[2] then
 * we will get exception because of we did'nt define here value of a[2]
 */
public class PrintTwovalueArray {
public static void main(String[] args){
	int[] [] a = new int [3][];
	a[0] = new int [4];
	a[1] = new int [5];
	System.out.println(a[1].length);
}
}
