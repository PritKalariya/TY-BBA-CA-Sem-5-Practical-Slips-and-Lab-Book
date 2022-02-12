// Define an abstract class Shape with abstract methods area() and volume(). Derive abstract class Shape into two classes Cone and Cylinder. Write a java Program to calculate area and volume of Cone and Cylinder.(Use Super Keyword.)


import java.util.Scanner;


abstract class Shape {
    float pi = 3.14f;
    abstract void area();
    abstract void volume();
}

class Cone extends Shape {
    int r, side, height;
    Cone(int r, int side, int height) {
        this.r = r;
        this.side = side;
        this.height = height;
    }

    void area() {
        float area = pi * r * side;
        System.out.println("Area of Cone: " + area);
    }

    void volume() {
        float volume = pi * r * r * (height / 3);
        System.out.println("Volume of Cone: " + volume);
    }
}

class Cylinder extends Shape {
    int r, side, height;
    Cylinder(int r, int side, int height) {
        this.r = r;
        this.side = side;
        this.height = height;
    }

    void area() {
        float area = 2 * pi * r * height + 2 * pi * r * r;
        System.out.println("Area of Cylinder: " + area);
    }

    void volume() {
        float volume = pi * r * r * height;
        System.out.println("Volume of Cylinder: " + volume);
    }
}


public class Q1_B {
    public static void main(String[] args) {
        int r, side, height;
        Scanner sc = new Scanner(System.in);

        try {
            System.out.println("Enter radius: ");
            r = sc.nextInt();
            System.out.println("Enter side: ");
            side = sc.nextInt();
            System.out.println("Enter height: ");
            height = sc.nextInt();

            Cone cone = new Cone(r, side, height);
            Cylinder cylinder = new Cylinder(r, side, height);

            cone.area();
            cone.volume();
            cylinder.area();
            cylinder.volume();

            sc.close();
        } catch (Exception e) {
            System.out.println("Invalid Input");
        }
    }
}