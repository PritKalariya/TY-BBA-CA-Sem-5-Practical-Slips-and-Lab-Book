// Write a java program to display transpose of a given matrix.


public class Q1_B {
    public static void main(String[] args) {
        int original_matrix[][] = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
        int transpose_matrix[][] = new int[3][3];

        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++) {
                transpose_matrix[j][i] = original_matrix[i][j];
            }
        }

        System.out.println("Original Matrix");
        for(int i = 0; i < 3; i++) {
            System.out.println();
            for(int j = 0; j < 3; j++) {
                System.out.print(original_matrix[i][j] + " ");
            }
        }

        System.out.println("\n\nTranspose Matrix");
        for(int i = 0; i < 3; i++) {
            System.out.println();
            for(int j = 0; j < 3; j++) {
                System.out.print(transpose_matrix[i][j] + " ");
            }
        }
    }
}