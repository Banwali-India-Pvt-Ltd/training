import java.util.*;
public class PrimeWhile {
public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	int num = sc.nextInt();
	int flag =0;
	int i=2; 
	
	while(i<num){
		if(num%i==0){
			
			System.out.println("Number is not prime");
		    flag =1;
			break;
		}
		i++;
	}
	
	if(flag==0){
		System.out.println("Number is prime");
	
	}
	sc.close();
}
}
