public abstract class Util {
    /*
    Add a method to check if a card is ok to play
    (public static boolean isLegal(Kaart toPut, Kaart bovensteKaart))
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
    public static boolean isLegal(Kaart omTeLeggen, Kaart bovensteStapel){
        if (omTeLeggen.getColor().equals(bovensteStapel.getColor())){
            return true;
        } else if (omTeLeggen.getIcoon().equals(bovensteStapel.getIcoon())){
            return true;
        } else if (omTeLeggen.getColor().equals("Black")){
            return true;
        } else {
            return false;
        }
    }
}
