import java.util.*;
public class Question10 {
public static void main(String[] args){
	Scanner sameer = new Scanner(System.in);
	int quantity = sameer.nextInt();
	int price = sameer.nextInt();
	int revenue = quantity*price;
	int disA = (revenue*10)/100;
	int disB = (revenue*15)/100;
	if(quantity>=100&&quantity<=120){
		revenue = revenue-disA;
	}
	else if(quantity>120){
		revenue = revenue-disB;
	}
	
	System.out.println(" Revenue is " + revenue);
	
	sameer.close();
	
	
}
}






