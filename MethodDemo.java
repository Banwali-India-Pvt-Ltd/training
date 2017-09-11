// The program creates two method int tpyes and return types
// class to create an object
public class MethodDemo 
{
	// main method to create program
	public static void main(String[] args)
	{
		MethodDemo obj = new MethodDemo();    // create an object to call method
		int x = obj.disp(10,15);              // store value in obj to call
		int y = obj.visp(20,15);              
		System.out.println(" value of disp x = " + x);    // display value which stored in x,y
		System.out.println(" value of visp y =" +y);
	}
	public int disp(int n1, int n2)          // create a disp function
	{
		
		return n1+n2;                        // return the value which have in n1,n2
		
	}
	public int visp(int v1, int v2)          // create visp method or function 
	{
		
		return v1-v2;                        // return the value which have in v1, v2
	}
	

}
