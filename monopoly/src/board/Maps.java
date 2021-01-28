package board;

import errors.AlreadyInisializedException;

public enum Maps {
    Nederland(null, null);
    private final Street[] straten;
    private final SpeciaalVak[] speciaal;

    Maps(Street[] straten, SpeciaalVak[] speciaal) {
        this.straten = straten;
        this.speciaal = speciaal;
        
    }

    public Street[] getStraten() {
        return straten;
    }

    public SpeciaalVak[] getSpeciaal() {
        return speciaal;
    }
    
    public Board getBoard() {
        Board board = new Board();
        try {
            board.addSpecials(speciaal);
            board.addStreets(straten);
        } catch (AlreadyInisializedException e) {
            System.out.println("An error accoured during inisializing the board. Please Ctrl+C out of the game. Here is the error message:");
            e.printStackTrace(); // will never happen.
        }
        return board;
    }
}
