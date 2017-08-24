import java.util.*;
public class PrimeNumbeR {
public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	int num = sc.nextInt();
	int i;
	for(i=2; i<num; i++){
		if(num%i==0){
		break;
		}
	}
		if(num==i){
			System.out.println("Number is prime");
		}
		else{
			System.out.println("Number is not prime");
		}
		sc.close();
		}
      
		
	}


