/* Write a java program to display following pattern:
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5 */


import java.util.Scanner;

public class Q1_A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of rows: ");
        int rows = sc.nextInt();

        for (int i = rows; i >= 1; i--) {
            for (int j = i; j <= rows; j++) {
                System.out.print(j + " ");
            }

            System.out.println();
        }
        sc.close();
    }
}