// Why I'm unable to write main method above side
// The program displays the value which is in the condition
// class to create method
public class NoReturn 
{
	// Create a Non-static method and returns nothing
	public void comparison()
	{
		int a = 50, b = 40;
		if(a>b)
		{
			System.out.println("A is a Big Number");
		}
		else 
		{
			System.out.println("B is a Big Number");
		}
	}
	public void main(String[] args)
	{
		// Create object
		NoReturn abc = new NoReturn();
		abc.comparison();
	}
}
