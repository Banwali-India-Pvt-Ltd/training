// The program gets ten name mark age of the persons
// import to create scannner class
import java.util.*;
// class to create method
public class NameMarkAvg 
{
	// main method to create program
public static void main(String[] args)
{
	// Scanner class to get inputs
	Scanner sc = new Scanner(System.in);
	// Loop to print ten datas
	for(int i=0; i<10; i++)
	{
	String name = sc.next();
	int age = sc.nextInt();
	int mark = sc.nextInt();
	
	NameMarkAvg Num = new NameMarkAvg();
	Num.disp(name, age, mark);
	}
}

public void disp(String name, int age, int mark) // instance method
{
	String x = name;
	int y = age;
	int z = mark;
	System.out.println(x);
	System.out.println(y);
	System.out.println(z);
}
}
