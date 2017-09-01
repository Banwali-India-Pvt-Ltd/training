// The program gives multiplication of the three numbers
// import to define Scannner class
import java.util.Scanner;
// class name to create object
public class MultiFuction {
	// main method to create program
	public static void main(String[] args){
		// Scanner class to get input
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		// create obj with name of class to calling
	MultiFuction Num = new MultiFuction();
	Num.disp(a,b,c);
	}
	
// create method
public void disp(int a, int b, int c ){
	int x = a;
	int y = b;
	int z = c;
	int p = x*y*z;
	System.out.print(p);
	
	
}
}
