import java.util.*;
public class Prime {
public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	int num = sc.nextInt();
	int flag=0;
	for(int i=2; i<num; i++){
		if(num%i==0){
			System.out.println("Number is Not Prime");
			flag=1;
			break;
		}
		}
	if(flag==0){
		System.out.println("Number is Prime");
	}
	sc.close();
}
}
