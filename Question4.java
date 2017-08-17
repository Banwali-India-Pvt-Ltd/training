import java.util.*;
public class Question4 {
public static void main(String[] args){
	Scanner sameer = new Scanner(System.in);
	 
	char ch=sameer.next( ).charAt(0);
	if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'||ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U'){
		System.out.println(ch + " is vowel");
	}
	else if((ch>='a'&&ch<='z')||(ch>='A'&&ch<='Z')){
		System.out.println(ch + " is a consonant");
		
	}
	else{
		System.out.println("Not an alphabet");
	}
	sameer.close();
}
}
