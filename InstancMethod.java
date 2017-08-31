
public class InstancMethod {
public static void main(String[] args){
	InstancMethod sc = new InstancMethod ();
	sc.disp(); // calling instance method
	
}
void disp() // instance method
{
	int a = 10; // local variable
	System.out.println(a);
}
}
