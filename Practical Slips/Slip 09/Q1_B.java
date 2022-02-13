// Write a java program to validate PAN number and Mobile Number. If it is invalid then throw user defined Exception "Invalid Data", otherwise display it


class InvalidDataException extends Exception {
    InvalidDataException(String string) {}
}


public class Q1_B {
    public static void main(String[] args) {
        String pan = "PAN123456789";
        String mobile = "1234567890";
        try {
            if(pan.length() != 10) {
                throw new InvalidDataException("Invalid PAN Number");
            }
            if(mobile.length() != 10) {
                throw new InvalidDataException("Invalid Mobile Number");
            }
            System.out.println("Valid PAN Number and Mobile Number");
        }
        catch(InvalidDataException e) {
            System.out.println("Invalid Data");
        }
    }
}