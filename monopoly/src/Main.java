import board.Board;
import board.SpeciaalVak;
import board.Street;
import errors.AlreadyInisializedException;
import errors.NotCompletedError;

public class Main {
    public static void main(String[] args) throws AlreadyInisializedException {
        Board board = new Board();
        board.addStreets(new Street(600, "1", 0, 20),
                new Street(600, "2", 2, 20),
                new Street(600, "3", 3, 20),
                new Street(600, "4", 4, 20),
                new Street(600, "5", 5, 20),
                new Street(600, "6", 6, 20),
                new Street(600, "7", 7, 20));
        board.addSpecials(new SpeciaalVak("s1", 0, 0, 1),
                new SpeciaalVak("s2", 0, 0, 8),
                new SpeciaalVak("s3", 0, 0, 9));
        System.out.println(board.toString());
        System.out.println("Dit programma is nog niet af. ");
        throw new NotCompletedError();
    }
}
