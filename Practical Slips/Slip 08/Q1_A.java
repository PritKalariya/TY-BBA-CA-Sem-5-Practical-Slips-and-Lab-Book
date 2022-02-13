// Define an Interface Shape with abstract method area(). Write a java program to calculate an area of Circle and Sphere.(use final keyword)


import java.util.*;


interface Shape {
    void area();
}


class Circle implements Shape {
    final float pi = 3.14f;
    float ac, r;
    Scanner sc = new Scanner(System.in);

    Circle() {
        System.out.println("Enter the radius of circle: ");
        r = sc.nextFloat();
    }

    public void area() {
        ac = pi * r * r;
        System.out.println("Area of circle is: " + ac);
    }
}

class Sphere implements Shape {
    final float pi = 3.14f;
    float ac, r;
    Scanner sc = new Scanner(System.in);

    Sphere() {
        System.out.println("Enter the radius of sphere: ");
        r = sc.nextFloat();
    }

    public void area() {
        ac = 4 * pi * r * r;
        System.out.println("Area of sphere is: " + ac);
    }
}

public class Q1_A {
    public static void main(String[] args) {
        Circle c = new Circle();
        Sphere s = new Sphere();
        c.area();
        s.area();
    }
}