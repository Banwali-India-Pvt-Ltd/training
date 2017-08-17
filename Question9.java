import java.util.*;
public class Question9 {
public static void main(String[] args){
	Scanner sameer = new Scanner(System.in);
	int quiz = sameer.nextInt();
	int mid = sameer.nextInt();
	int finalscore = sameer.nextInt();
	int total = quiz+mid+finalscore;
	int multi = total*100;
	int averagescore = multi/300;
	if(averagescore>=90){
		System.out.println("A");
	}
	else if(averagescore>=70&&averagescore<90){
		System.out.println("B");
	}
	else if(averagescore>=50&&averagescore<70){
		System.out.println("C");
	}
	else if(averagescore<50){
		System.out.println("F");
	}
	sameer.close();
}
}
