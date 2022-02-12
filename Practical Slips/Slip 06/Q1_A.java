// Write a java program to accept a number from user, if it zero then throw user defined Exception "Number Is Zero", otherwise calculate the sum of first and last digit of that number. (Use static keyword).


import java.util.Scanner;
import java.io.*;

class NumberIsZeroException extends Exception {
    NumberIsZeroException() {}
}

class Number {
    static int no;
    Number() throws IOException {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter no: ");
            no = sc.nextInt();
        }
        try {
            if (no == 0) {
                throw new NumberIsZeroException();

            }
            cal();
        } catch (NumberIsZeroException e) {
            System.out.println("Number is zero");
        }

    }

    void cal() {
        int f = 0, l = 0;
        f = no % 10;
        if (no > 9) {
            while (no > 0) {
                l = no % 10;
                no = no / 10;
            }
            System.out.println("Addition of first and last digit = " + (f + l));
        } else {
            System.out.println("Addition of first and last digit = " + f);
        }
    }
}


public class Q1_A {
    public static void main(String[] args) throws IOException {
        Number n = new Number();
    }
}