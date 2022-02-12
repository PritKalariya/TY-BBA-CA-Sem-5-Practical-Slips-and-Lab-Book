// Write a java program to display all the vowels from a given string.


import java.util.Scanner;

public class Q1_A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a string: ");
        String str = sc.nextLine();
        str = str.toLowerCase();

        System.out.println("Vowels are: ");
        for(int i=0; i<str.length(); i++) {
            if(str.charAt(i) == 'a' || str.charAt(i) == 'e' || str.charAt(i) == 'i' || str.charAt(i) == 'o' || str.charAt(i) == 'u') {
                System.out.println(" " + str.charAt(i));
            }
        }

        sc.close();
    }
}