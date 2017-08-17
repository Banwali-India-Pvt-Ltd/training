import java.util.*;
public class Question7 {
public static void main(String[] args){
	Scanner sameer = new Scanner(System.in);
	int age = sameer.nextInt();
	if(age>=18){
		System.out.println("You are eligible to vote");
	}
	else{
		System.out.println("You are not eliglibe to vote");
		
	}
	sameer.close();
	
}
}
