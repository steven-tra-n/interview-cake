import MergeIntervals.*;
import HashMaps.*;

public class main{
    public static void main(String[] args){
        System.out.println("Hello World!");

        Rectangle lover1 = new Rectangle(1, 1, 6, 3);
        Rectangle lover2 = new Rectangle(8, 5, 3, 6);

        System.out.println(RectangularLove.findLove(lover1, lover2));

        System.out.println(WordCloud.Generate("After beating the eggs, Dana read the next step:"));
        System.out.println(WordCloud.Generate("Add milk and eggs, then add flour and sugar."));
    };
};