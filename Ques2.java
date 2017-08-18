import java.util.*;
public class Ques2 {
public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	int  rem, sum = 0;
	int temp = n;
	while(n!=0){
		rem = n% 10;
		sum = (sum*10)+rem;	
		n = n/10;
	}
	if(temp==sum){
		System.out.println("Palindrome");
	}
	else{
		System.out.println("Not Palindrome");
	}
	sc.close();
	}  
	}  
		
	
