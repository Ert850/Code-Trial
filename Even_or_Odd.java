import java.util.Scanner;
public class Even_or_Odd {
    public static void main(String[] args){
        int numToTest = 0;
        boolean validInput = false;
        String garbage = "";
        Scanner input = new Scanner(System.in);

        System.out.println("Enter an integer (whole number) to find out if it is Even or Odd\n");

        do{
            if(input.hasNextInt()){
                numToTest = input.nextInt();
                validInput = true;
            }
            else{
                garbage = input.nextLine();
                System.out.print("\n\"" + garbage + "\" is not a valid input, please try again\n" );
                validInput = false;
            }
        }while(validInput == false);

        if(numToTest % 2 == 0){
            System.out.println(numToTest + " is a even number");
        }
        else{
            System.out.println(numToTest + " is an odd number");
        }
    }
}
