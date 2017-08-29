import java.util.*;
public class InputCalculation {
public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	int [][] num = new int[3][4];
	for(int i=0; i<3; i++)
	{
		for(int j=0; j<4; j++)
		{
			num[i][j] = sc.nextInt();
		}
	}
	for(int i=0; i<3; i++)
	{
		for(int j=0; j<4; j++)
		{
			System.out.println(num[i][j]);
		}
		num[2][1] = num[1][0] + 60;
		
	}
	sc.close();
	
	
 	
	
}
}
