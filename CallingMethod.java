/* The problem is that how the program calling methods 
 * How the program is working by step by step ?
 * Why required to implement object anywhere ?
 */
public class CallingMethod {
// Create Non-static methods
	public int add()
	{
		int a = 10, b = 20;
		int result = a+b;
		return result;
	}
	public int add2()
	{
		int c = 100;
		CallingMethod obj = new CallingMethod();
		int res = (obj.add()) + c;
		return res;
	}
	// Create static methods
	public static int sub1()
	{
		int a = 100, b = 30;
		CallingMethod obj = new CallingMethod();
		int val = obj.add();
		int result = (a-b) - val;
		return result;
	}
	public static int sub2()
	{
		int a = 10, b = 7;
		int val = sub1();
		int result = (a-b) + val;
		return result;
	}
	public static void main(String[] args)
	{
		CallingMethod obj2 = new CallingMethod();
		int x = obj2.add();
		int y = obj2.add();
		
		System.out.println(x);  // 30
		System.out.println(y);  // 130
		
		System.out.println(sub1());  // 40
		System.out.println(sub2());  // 43
	}
}
