public abstract class Util {
    /*
    calculate winner (public static int get_winner, return -1 if there is no winner)
    add a method to hide the cards (public static void hide())
    */

    public static int getWinner(Speler[] spelers) {
        for (Speler speler : spelers) {
            if (speler.getKaarten().toArray().length == 0) {
                return speler.getSpelerNummer();
            }
        }
        return -1;
    }

    public static void hide(){
        for (int i = 0; i < 2000; i++) {
            System.out.println();
        }
    }
}
