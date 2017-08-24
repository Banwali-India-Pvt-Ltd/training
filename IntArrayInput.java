import java.util.*;
public class IntArrayInput {
public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	int[] marks = new int[5];
	
	for(int i=0; i<5; i++){
		marks[i] = sc.nextInt();
	}
	for(int j=0; j<5; j++){
		System.out.println("Marks are = "+ marks[j]);
	}
	sc.close();
	
}
}
