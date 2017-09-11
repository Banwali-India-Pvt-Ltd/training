// The program gives return total by return type way
// class to create an object
public class CallMethod 
{
	// main method to create program
	
 public static void main(String[] args)
 {
      CallMethod obj = new CallMethod();          // create an object to call method
       int b = obj.total();                       // assign method name in b
       System.out.println(b);                     // display b 

}
 public  int total()                            // create total method in return type
{
	int a = 10+10;                              // store number of value in a
	return a;
}
}
