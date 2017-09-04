// The program defining method(Function) in the main method

// class to create object

public class FunctionQuora {
	// main method to create program
public static void main(String[] args)
{
	
	// define rank of students to implement method
	studentRank(499);
}
public static void studentRank(int marks) // method with name of student marks not returnable 
{
	// implement the condition to get true or false
	if(marks>=600)
	{
		System.out.println("Rank:A1");
	}
	else if(marks>=500)
	{
		System.out.println("Rank:A2");
	}
	else
	{
		System.out.println("Rank:A3");
	}
}
}
