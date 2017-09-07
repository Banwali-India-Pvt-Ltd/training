// Same problem why not main method above side
// The program is a static and checks weather the value is greater or not
// class to create object
public class NoReturnStatic
{
    // Create a static method and returns nothing
	public static void comparision()
	{
		int a = 100, b = 20;
		if(a>b)
		{
			System.out.println("A is a Big Number");
		}
		else 
		{
			System.out.println("B is a Big Number");
		}
	}
	public static void main(String[] args){
		NoReturnStatic.comparision();
		
	}
}
