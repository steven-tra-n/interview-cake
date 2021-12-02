package MergeIntervals;

public class RectangularLove {
    public static Rectangle findLove(Rectangle lover1, Rectangle lover2){
        Rectangle result = new Rectangle(0, 0, 0, 0);

        // 1. Find x overlap
        // 2. Find y overlap

        // 1
        int[] xOverlap = findOverlap(lover1.getLeftX(), lover1.getWidth(), lover2.getLeftX(), lover2.getWidth());

        // 2
        int[] yOverlap = findOverlap(lover1.getBottomY(), lover1.getHeight(), lover2.getBottomY(), lover2.getHeight());

        result = new Rectangle(xOverlap[0], yOverlap[0], xOverlap[1], yOverlap[1]);

        return result;
    };

    public static int[] findOverlap(int point1Start, int dimension1, int point2Start, int dimension2){
        // Assumes that inputs are sorted on their points
        int start = Math.max(point1Start, point2Start);
        int end = Math.min((point1Start + dimension1), (point2Start + dimension2));

        if(start > end){
            return new int[] {0, 0};
        };

        return new int[] {start, end};
    };  
};

// System.out.println("Hello World!");

//         Rectangle lover1 = new Rectangle(1, 1, 6, 3);
//         Rectangle lover2 = new Rectangle(8, 5, 3, 6);

//         System.out.print(RectangularLove.findLove(lover1, lover2));