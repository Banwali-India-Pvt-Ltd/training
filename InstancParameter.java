// The Program which is instance method with parameter in
// class to create method
public class InstancParameter {
	// main method to create program
public static void main(String[] args){
	InstancParameter sc = new InstancParameter();
	sc.disp(10,20); // calling instance method & passing values
	
}
void disp(int a, int b) // Instance method with parameter
{
	int c = a+b; // local variable
	System.out.println(c);
}
}
