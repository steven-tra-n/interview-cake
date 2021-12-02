import MergeIntervals.*;

public class main{
    public static void main(String[] args){
        System.out.println("Hello World!");

        Rectangle lover1 = new Rectangle(1, 1, 6, 3);
        Rectangle lover2 = new Rectangle(8, 5, 3, 6);

        System.out.print(RectangularLove.findLove(lover1, lover2));
    };
};