// The program returns string with instance method
// class to create an object
public class StringReturn 
{
	// main method to create program
	public static void main(String[] args)
	{
		StringReturn obj = new StringReturn();     // Create an object with class name
		System.out.println(obj.fname());
		
	}
    
	String fname()                 // Instance Method
	{
		String s = "Banwali";      // Local variable
		return s;
	}
	}

