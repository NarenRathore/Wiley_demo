import java.util.Scanner;
public class Main
{
    //this method takes array of intergers as input as return the average 
    public static double Average(int[] arr){
        double sum=0;
        for(int i:arr)  //iterate over the intergers in array
            sum+=i;     //add them to sum
        //divide sum by number of elements in array to get average
        sum=sum/arr.length;
        //return sum 
        return sum;
    }
