package board;

import errors.AlreadyInisializedException;
import player.Player;
import util.Data;

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

    public String toString(){
        StringBuilder returnValue = new StringBuilder();
        short streetIndex = 0;
        short specialIndex = 0;
        for (short i = 0; i < 10; i++) {
            if (Data.searchForInArray(straten, new Street(i)) == -1){
                returnValue.append(String.format("%-20s", speciaal[specialIndex].getNaam()));
                specialIndex++;
            } else {
                returnValue.append(String.format("%-20s", straten[streetIndex].getNaam()));
                streetIndex++;
            }
        }
        streetIndex = 0;
        specialIndex = 0;
        returnValue.append(String.format("%n"));
        for (short i = 0; i < 10; i++) {
            if (Data.searchForInArray(straten, new Street(i)) == -1){
                returnValue.append(String.format("%-20s", speciaal[specialIndex].getEuroBijTeTellen()));
                specialIndex++;
            } else {
                returnValue.append(String.format("%-20s", straten[streetIndex].getPrijs()));
                streetIndex++;
            }
        }
        returnValue.append(String.format("%n"));
        return returnValue.toString();
    }
}
