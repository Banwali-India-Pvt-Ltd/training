
public class SwitchMethod {
public static void main(String[] args){
	char  grade = 'C';
	switch(grade){
	case 'A':
		System.out.println("Excellent!");
		break;
	case 'B':
		
	case 'C':
		System.out.println("Welldone");
		break;
	case 'D':
		System.out.println("You passed");
		break;
	case 'F':
		System.out.println("Better try again");
		break;
	default:
		System.out.println("Invalid grade");
		
	}
	System.out.println("Your grade is " + grade);
}
}
