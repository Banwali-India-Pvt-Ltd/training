// The program create an object and returns value by data types
// class to create method
public class DataTypes 
{
	// main method to create program
	public static void main(String[] args)
    {
        Double object = new Double("1.5");  // create object with Double
        
        int a = object.intValue();
        byte b = object.byteValue();
        double c = object.doubleValue();
        float d = object.floatValue();
        
 
        System.out.println(c);  // returns 1.5
        System.out.println(d);  // returns 1.5
        System.out.println(a);  // returns 1
        System.out.println(b);  // returns 1
        System.out.println(a+b+c+d);  // returns total of all
 
    }
}
