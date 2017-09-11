// The program returns two string by two ways
// class to create an object
public class StringReturnTwo 
{
	// main method to create program
	public static void main(String[] args)
	{
		StringReturnTwo obj = new StringReturnTwo();
		System.out.println(obj.aname());
		
		String name = obj.bname("Company");
		System.out.println(name);
	}
	String aname()                  // Instance method
	{
		String s = "Banwali";       // local variable
		return s;
	}
	String bname(String st)        // Instance method
	{
		String str = st;           // local variable
		return str;
	}

}
