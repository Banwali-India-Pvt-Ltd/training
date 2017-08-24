import java.util.Scanner;

public class StringArray {
public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	String[] names = new String [10];
	for(int i=0; i<10; i++){
		names[i] = sc.next();
	}
	for(int j=0; j<10; j++){
		System.out.println(names[j]);
	}
	sc.close();
}
}
