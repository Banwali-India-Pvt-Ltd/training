// Need to understand this program as well 
public class Parameter {
	 public static void main(String[] args)
	    {
	        String obj1 = new String("geeks");
	        String obj2 = new String("geeks");
	 
	        if(obj1.hashCode() == obj2.hashCode())
	            System.out.println("hashCode of object1 is equal to object2");
	 
	        if(obj1 == obj2)
	            System.out.println("memory address of object1 is same as object2");
	 
	        if(obj1.equals(obj2))
	            System.out.println("value of object1 is equal to object2");
	    }
	   
}