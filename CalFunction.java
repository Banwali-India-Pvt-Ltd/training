// The program returns the value in several data types 
// class to create an object
public class CalFunction 
{
	public double calculation(double x, double y)   // create double type method
	{
		return x+y;
	}
	public void calculation(int x, double y)       // create void method
	{
		double s = x+y;
		System.out.println("Value of int & double = " +s);
	}
	public int calcualation(int x, int y)        // create integer type method
	{
		return x+y;
	}
	
	// main method to create program
	public static void main(String[] args)
	{
		CalFunction obj = new CalFunction();     // create an object to call
		int a = obj.calcualation(145, 125);      // call int method
		double b = obj.calculation(14.5, 1.25);   // call double method
		obj.calculation(11, 11.43);
		System.out.println("Value of int & int = " + a);
		System.out.println("Value of double & double = " +b);
		
		
	}

}
