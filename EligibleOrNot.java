import java.util.*;
public class EligibleOrNot {
public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	String name = sc.next();
	String gender = sc.next();
	int age = sc.nextInt();
	
	if(gender.equalsIgnoreCase("Male")){
		if(age>=21){
			System.out.println(name + " is eligible");
			
		}
		else{
			System.out.println(name + " is not eligible");
		}
		
	}
	if(gender.equalsIgnoreCase("Female")){
		if(age>=18){
			System.out.println(name + " is eligible");
		}
		else{
			System.out.println(name + " is not eligible");
		}
	}
	sc.close();
}
}
