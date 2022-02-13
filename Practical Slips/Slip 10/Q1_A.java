// Write a java program to count the frequency of each character in a given string.


public class Q1_A {
    public static void main(String[] args) {
        String str = "Java is a programming language";
        int[] freq = new int[str.length()];
        char string[] = str.toCharArray();

        for (int i = 0; i < string.length; i++) {
            for (int j = 0; j < string.length; j++) {
                if (string[i] == string[j]) {
                    freq[i]++;
                }
            }
        }

        System.out.println("The frequency of each character in the given string is: ");
        for (int i = 0; i < freq.length; i++) {
            if(string[i] != ' ' && string[i] != '0') {
                System.out.println(string[i] + " : " + freq[i]);
            }
        }
    }
}