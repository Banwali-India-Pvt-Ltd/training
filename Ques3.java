import java.util.*;
public class Ques3 {
public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	int a = sc.nextInt();
	
	int sum=0, rem, temp;
	int number = a;
	temp = number;
	while(number>0){
		rem = number%10;
		number = number/10;
		sum += (rem*rem*rem);
	}
	if(sum==temp){
		System.out.println("Number is ArmStrong");
	}
	else{
		System.out.println("Number is Not ArmStrong");
	}
	sc.close();
}
}