public abstract class Util {
    /*
    calculate winner (public static int get_winner, return -1 if there is no winner)

    */

    public static int getWinner(Speler[] spelers){
         for (Speler speler : spelers) {
            if (speler.getKaarten().toArray().length == 0) {
                return speler.getSpelerNummer();
            }
        }
        return -1;
    }
}
