// The Program creates two class and give the addition
// main class to create object
public class InstaneInAnoClass {
	// main method to create program
public static void main(String[] args){
	// Addition obj to call value
	Addition sc = new Addition();
	sc.disp(20);
}
}
// create another class with name of obj
class Addition{
	// calling a
public void disp(int a)  // instance method
{ 
	int x = 10; 
	int y = a;
	int z = x+y;
	System.out.println(z);
}
}