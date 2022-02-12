// Write a ‘java’ program to check whether given number is Armstrong or not. (Use static keyword)


import java.util.Scanner;
import java.lang.Math;


public class Q1_A {
    static boolean isArmstrong(int n) {
        int sum = 0;
        int temp = n;
        while (n > 0) {
            int r = n % 10;
            sum += Math.pow(r, 3);
            n /= 10;
        }
        return (sum == temp);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = sc.nextInt();
        if (isArmstrong(n)) {
            System.out.println("The number is Armstrong");
        } else {
            System.out.println("The number is not Armstrong");
        }
        sc.close();
    }
}