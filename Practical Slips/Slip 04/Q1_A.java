// Write a java program to display alternate character from a given string.


import java.util.Scanner;

public class Q1_A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = "";
        int i = 0;
        System.out.println("Enter a string: ");
        str = sc.nextLine();
        while (i < str.length()) {
            if (i % 2 == 0) {
                System.out.print(str.charAt(i));
            }
            i++;
        }
        sc.close();
    }
}