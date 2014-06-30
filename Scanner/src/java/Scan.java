/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Shantanu
 */
import java.util.Scanner;
public class Scan {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int b = input.nextInt();
        int c;
        try
        {
        c = a/(b-b);
        System.out.println(c);
        }
        catch(ArithmeticException);
        {
            System.out.println("Exception");
        }
        finally
        {
            System.out.println("Final");
        }
        
    }
    
}
