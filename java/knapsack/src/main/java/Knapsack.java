/*
Since this exercise has a difficulty of > 4 it doesn't come
with any starter implementation.
This is so that you get to practice creating classes and methods
which is an important part of programming in Java.
Please remove this comment when submitting your solution.
*/
import java.util.ArrayList;
public class Knapsack {

    public int maximumValue(int capacity, ArrayList<Item> items) {
        int[][] a = new int[items.size()+1][capacity+1];
        for (int i = 1; i <= items.size(); i++) {
            int vi = items.get(i-1).value;
            int wi = items.get(i-1).weight;
            for (int w = 0; w <= capacity; w++)
                if (w < wi) a[i][w] = a[i-1][w];
                else        a[i][w] = Math.max(a[i-1][w-wi]+vi, a[i-1][w]);
        }
        return a[items.size()][capacity];
    }
}
