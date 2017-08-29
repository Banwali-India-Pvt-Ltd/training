
public class Marks2Darray {
public static void main(String[] args){
	int [][] studentmark = {{10,20,30},{40,50,60}, {70,80,90}};
	for(int i=0; i<studentmark.length; i++)
	{
		for(int j=0; j<studentmark[i].length; j++){
			System.out.println(studentmark[i][j]);
		}
		
	}
	System.out.println(studentmark.length);
}
}
