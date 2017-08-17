import java.util.*;
public class Question3 {
public static void main(String[] args){
	Scanner sameer = new Scanner(System.in);
	int n = sameer.nextInt();
	int j = sameer.nextInt();
	if((j%2==1)&&(j%3==0)){
		System.out.println("Odd");
	}
	else if(n%2==0){
		System.out.println("Even");
	}
	else{
		System.out.println("Not match");
	}
	sameer.close();
}
}
