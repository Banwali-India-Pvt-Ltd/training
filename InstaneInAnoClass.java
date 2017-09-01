
public class InstaneInAnoClass {
public static void main(String[] args){
	Addition sc = new Addition();
	sc.disp(20);
}
}
class Addition{
public void disp(int a){
	int x = 10; 
	int y = a;
	int z = x+y;
	System.out.println(z);
}
}