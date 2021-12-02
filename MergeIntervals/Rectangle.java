package MergeIntervals;

public class Rectangle {
    // coordinates of bottom left corner
    private int leftX;
    private int bottomY;
    
    // dimensions
    private int width;
    private int height;

    public Rectangle(int leftX, int bottomY, int width, int height){
        this.leftX = leftX;
        this.bottomY = bottomY;
        this.width = width;
        this.height = height;
    };

    public int getLeftX(){
        return leftX;
    };

    public int getBottomY(){
        return bottomY;
    };

    public int getWidth(){
        return width;
    };

    public int getHeight(){
        return height;
    };
};