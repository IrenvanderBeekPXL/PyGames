package board;

import errors.AlreadyInisializedException;
import player.Player;

public class Board {
    private Street[] straten = null;
    private SpeciaalVak[] speciaal = null;
    private Player[] spelers = null;
    private short lengte = 0;

    public void addStreets(Street... streets) throws AlreadyInisializedException {
        if (straten == null){
            straten = streets;
            lengte += streets.length;
        } else {
            String msg = "Streets already inisialized";
            throw new AlreadyInisializedException(msg);
        }
    }
    public void addSpecials(SpeciaalVak... specialeVakken) throws AlreadyInisializedException {
        if (speciaal == null){
            speciaal = specialeVakken;
            lengte += specialeVakken.length;
        } else {
            String msg = "Specials already inisialized";
            throw new AlreadyInisializedException(msg);
        }
    }
    public void addPlayers(Player... streets) throws AlreadyInisializedException {
        if (spelers == null){
            spelers = streets;
        } else {
            String msg = "Players already inisialized";
            throw new AlreadyInisializedException(msg);
        }
    }

    public short getLengte() {
        return lengte;
    }
}
