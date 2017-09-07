/* The program extends another class
 * And print sum of the numbers
 */
// class to create object & extends to get another class method
public class Class2  extends Class1 
{
	
	    // main method to create program
		public static void main(String[] args)
		{
			Class2 obj = new Class2();
			int x = obj.add(12, 23);
			System.out.println(x);  // 35
}
}
