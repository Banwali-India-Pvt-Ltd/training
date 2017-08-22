import java.util.*;
public class Palindrome {
public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	int a = sc.nextInt();
	int t = a;
	int r, sum = 0;
	while(a>0){
		r = a%10;
		a = a/10;
		sum = sum*10+r;
		
	}
	if(t==sum){
		System.out.println("Number is Palindrome");
	}
	else{
		System.out.println("Number is Not Palindrome");
	}
	sc.close();
}
}
