import java.util.*;

public class javabasics{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        // System.out.print("First programm for java : ");
        // float a=sc.nextFloat();
        // int b=(int)a;
        // System.out.println("The value of b is: "+b);
        // int age=22;
        // if(age>18){
        //     System.out.println("You can drive and vote and etc");
        // }
        // else{
        //     System.out.println("You cannot drive");
        // }
        // int number=sc.nextInt();
        // switch(number){
        //     case 1:
        //         System.out.println("Monday");
        //         break;
        //     case 2:
        //         System.out.println("Tuesday");
        //         break;
        //     case 3:
        //         System.out.println("wednesday");
        //         break;
        //     default:
        //         System.out.println("switch completed");
        // }
        // for(int i=0;i<5;i++){
        //     System.out.println("*".repeat(i));
        // }

        //************************************patterns******************** */
        //Star Pattern
        // System.out.print("Enter a number of star pattern: ");
        // int n=sc.nextInt();
        // for(int i=1;i<=n;i++){
        //     for(int j=1;j<=i;j++){
        //         System.out.print("*");  
        //     }
        //     System.out.println();
        // }

        // //Inverted Star Pattern
        // System.out.print("Enter a number of star pattern: ");
        // int m=sc.nextInt();
        // for(int i=m;i>0;i--){
        //     for(int j=1;j<=i;j++){
        //  System.out.print("*");  
        //     }
        //     System.out.println();
        // }

        //half pyrammid pattern
        // System.out.print("Enter a number to print half pyrammid : ");
        // int m=sc.nextInt();
        // for(int i=1;i<=m;i++){
        //     for(int j=1;j<=i;j++){
        //         System.out.print(j);
        //     }
        //     System.out.println();
        // }
        
        
        //character pyrammid pattern
           System.out.print("Enter a number to character pattern : ");
        int m=sc.nextInt();
        char ch='A';
        for(int i=1;i<=m;i++){
            for(int j=1;j<=i;j++){
                System.out.print(ch);
                ch++;
            }
            System.out.println();
        }
        sc.close();
    }
}