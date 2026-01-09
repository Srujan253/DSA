import java.util.*;

public class javabasics{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("First programm for java : ");
        float a=sc.nextFloat();
        int b=(int)a;
        System.out.println("The value of b is: "+b);
        int age=22;
        if(age>18){
            System.out.println("You can drive and vote and etc");
        }
        else{
            System.out.println("You cannot drive");
        }
        
        sc.close();
    }
}