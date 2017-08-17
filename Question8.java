import java.util.*;
public class Question8 {
public static void main(String[] args){
	Scanner sameer = new Scanner(System.in);
	int age = sameer.nextInt();
	String gender = sameer.next();
	if(gender.equalsIgnoreCase("Male")){
		if(age>=21){
			System.out.println("Eligible");
		}
		else{
			System.out.println("Not eligible");
		}
		
	}
	else if(gender.equalsIgnoreCase("Female")){
		if(age>=18){
			System.out.println("Eligible");
		}
		else{
			System.out.println("Not eligible");
		}
	}
	sameer.close();
	
}
}
