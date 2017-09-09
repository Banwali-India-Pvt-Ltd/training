/* In this program I'm not getting that 
 * How it calling and why can't we change tha data type 
 * and names, values
 */
public class DisplayOverloading {
	public static void main(String args[])
	   {
	       DisplayOverloading obj = new DisplayOverloading();
	       obj.disp('s');
	       obj.disp('a',20);
}
	public void disp(char c)
    {
         System.out.println(c);
    }
    public void disp(char c, int num)  
    {
         System.out.println(c + " "+num);
    }
}