// public  Write a ‘java’ program to copy only non-numeric data from one file to another file.


import java.io.*;

public class Q1_B {
    public static void main(String[] args) {

        try {
            int i;

            FileInputStream fin = new FileInputStream("file1.txt");
            FileOutputStream fout = new FileOutputStream("file2.txt");

            try {
                do {
                    i = fin.read();
                    char ch = (char)i;

                    if(ch>='A' && ch<='Z' || ch>='a' && ch<='z') {
                        if(i!=-1) {
                            fout.write(i);
                        }
                    }
                } while(i!=-1);
                System.out.println("File copied successfully");
                fin.close();
                fout.close();
            }
            catch(IOException e) {
                System.out.println("Error in copying file");
            }
        }
        catch(FileNotFoundException e) {
            System.out.println("File not found");
        }
    }
}