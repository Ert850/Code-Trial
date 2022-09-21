import java.util.Scanner;
public class Even_or_Odd {
    public static void main(String[] args){
        int numToTest;
        Scanner input = new Scanner(System.in);

        System.out.println("Enter an integer (whole number) to find out if it is Even or Odd\n");
        numToTest = input.nextInt();

        if(numToTest % 2 == 0){
            System.out.println(numToTest + " is a even number");
        }
        else{
            System.out.println(numToTest + " is an odd number");
        }
    }
}
