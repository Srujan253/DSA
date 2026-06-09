import java.util.*;

public class functions{

    public  int add(int x, int y){
        return x+y;
    }

    public int factorial(int n){
        if(n==0 || n==1){
            return 1;
        }else{
            return n*factorial(n-1);

        }
        }
    public int fibonacci(int n){
        if(n==0){
            return 0;
        }else if(n==1){
            return 1;
        }else{
            return fibonacci(n-1)+fibonacci(n-2);

        }
        }
    
    
    public static void main(String[] args){
        functions obj=new functions();
        Scanner sc=new Scanner(System.in);
        // int a=5;
        // int b=10;
        // int sum=obj.add(a,b);
        // System.out.println("The sum of a and b is: "+sum);
        System.out.print("Enter the number to find the factorial: ");
        int num=sc.nextInt();
        int fact=obj.factorial(num);
        System.out.println("The factorial of "+num+" is: "+fact);

        System.out.print("Enter the number to find the fibonacci: ");
        int n=sc.nextInt();
        int fib=obj.fibonacci(n);
        System.out.println("The fibonacci of "+n+" is: "+fib);

    }

}