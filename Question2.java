import java.util.*;
public class Question2 {
public static void main(String[] args){
	Scanner sameer = new Scanner(System.in);
	int n = sameer.nextInt();
	int number = sameer.nextInt();
	
	if((n%2==0)&&(number%4==0)){
		System.out.println("Even");
	
	}
	
	else if(n%2==1){
		System.out.println("Odd");
	}
	else{
		System.out.println("Not match");
	
}
	sameer.close();
}
}