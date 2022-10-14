public class TinyLife {
    public static void main(String[] args) throws Exception{

    }
    long oscillator = 0x20272000037303L;
    long glider = 0x20A0600000000000L;

    public static boolean getCell(long world,int col, int row){



    }
    public static long setCell(long world, int col, int col, int row, boolean value){



    }
    public static void print(long world){
        System.out.println("-");
        for (int row = o;row<8;row++){
            for (int col = 0; col < 8;col++){
                System.out.print(getCell(world,col,row)?"#":"_");
            }
            System.out.println();
        }
    }
    public static int countNeighbours(long world, int col, int row){}
    public static boolean computeCell(long world,int col, int row){}
    public static long nextGeneration(long world){}
}
