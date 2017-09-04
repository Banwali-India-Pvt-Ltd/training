// The program return total of the values. I need to understand about return value
public class MethodOverloading {
	public static void main (String []args){
		 int x = add(5, 7);
		 int y = add(5, 7, 9);
		 double z = add(5.234, 7.23);
		 System.out.println(x);
		 System.out.println(y);
		 System.out.println(z);
}
	public static int add(int a, int b){
		 int result;
		 result = a + b;
		 return result;
		}
		public static int add(int a, int b, int c){
		 int result;
		 result = a + b + c;
		 return result;
		}
		public static double add(double a, double b){
		 double result;
		 result = a + b;
		 return result;
		}
		}
