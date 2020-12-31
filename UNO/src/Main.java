import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        boolean normale_volgorde = false;
        int spelerNummerAanDeBeurt = 0;
        Speler spelerAanDeBeurt = null;
        Kaart[] kaarten = VoegKaartenToe.addKaarten(2, 2, 4);
        Kaart bovensteKaart = kaarten[1];
        Scanner input = new Scanner(System.in);
        System.out.println("Hoeveel spelers?");
        Speler[] spelers = new Speler[input.nextInt()];
        for (int i = 0; i < spelers.length; i++) {
            spelers[i] = new Speler(i, kaarten);
        }
        while (Util.getWinner(spelers) == -1){
            // getting the correct player
            spelerNummerAanDeBeurt %= spelers.length;
            for (Speler speler : spelers) {
                if (speler.getSpelerNummer() == spelerNummerAanDeBeurt) {
                    spelerAanDeBeurt = speler;
                    break; // less cpu time
                }
            }

            // show the top card
            System.out.println("top card: " + bovensteKaart);

            // show the cards
            System.out.println("jouw kaarten:");
            assert spelerAanDeBeurt != null;
            for (Object kaart: spelerAanDeBeurt.getKaarten().toArray()) {
                System.out.println(kaart);
            }

            // ask the correct card for input
            System.out.println("Welke index kaaart wil je? (bovenste is index 1) ");
            bovensteKaart = spelerAanDeBeurt.popKaart(
                    Data.minMax(0, spelerAanDeBeurt.getKaarten().toArray().length - 1,
                            input.nextInt() - 1));

            // doing special stuff if needed
            // get next player
            int spelerNummerNext = spelerNummerAanDeBeurt + 1;
            Speler spelerNext = null;
            spelerNummerNext %= spelers.length;
            for (Speler speler : spelers) {
                if (speler.getSpelerNummer() == spelerNummerNext) {
                    spelerNext = speler;
                    break; // less cpu time
                }
            }
            if (bovensteKaart.getIcoon().equals("+2")){
                spelerNext.drawKaart(kaarten);
                spelerNext.drawKaart(kaarten);
                spelerNummerAanDeBeurt += 1;
            }
            if (bovensteKaart.getIcoon().equals("SKIP")){

            }
        }
    }
}
