import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        boolean normale_volgorde = true;
        int spelerNummerAanDeBeurt = 0;
        Speler spelerAanDeBeurt = null;
        Kaart[] kaarten = VoegKaartenToe.addKaarten(2, 2, 4);
        Kaart bovensteKaart = kaarten[1];
        Scanner input = new Scanner(System.in);
        System.out.println("Hoeveel spelers?");
        Speler[] spelers = new Speler[input.nextInt()];
        String newColor = "";
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
            System.out.println("Speler " + spelerNummerAanDeBeurt + " is aan de beurt");
            System.out.println("Druk op enter...");
            input.nextLine();
            input.nextLine();

            // show the top card
            System.out.println("top card: " + bovensteKaart);
            if (bovensteKaart.getColor().equals("Black")){
                System.out.println("Er moet iets op van kleur " + newColor);
            }

            // show the cards
            System.out.println("jouw kaarten:");
            assert spelerAanDeBeurt != null;
            for (Object kaart: spelerAanDeBeurt.getKaarten().toArray()) {
                System.out.println(kaart);
            }

            // ask the correct card for input
            System.out.println("Welke index kaaart wil je? (bovenste is index 1, 0 is draw) ");
            try {
                int legKaart = Data.minMax(-1, spelerAanDeBeurt.getKaarten().toArray().length - 1,
                        input.nextInt() - 1);
                // control if it is correct
                while (!Util.isLegal(spelerAanDeBeurt.getKaarten().get(legKaart), bovensteKaart, newColor)){
                    System.out.println("Error, deze kaart is ongeldig.");
                    System.out.println("Welke index kaaart wil je? (bovenste is index 1, 0 is draw) ");
                    legKaart = Data.minMax(-1, spelerAanDeBeurt.getKaarten().toArray().length - 1,
                            input.nextInt() - 1);
                }
                bovensteKaart = spelerAanDeBeurt.popKaart(legKaart);
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
                if (!bovensteKaart.getColor().equals("Black")) {
                    if (bovensteKaart.getIcoon().equals("+2")) {
                        spelerNext.drawKaart(kaarten);
                        spelerNext.drawKaart(kaarten);
                        spelerNummerAanDeBeurt += 1;
                    }
                    if (bovensteKaart.getIcoon().equals("SKIP")) {
                        spelerNummerAanDeBeurt += 1;
                    }
                    if (bovensteKaart.getIcoon().equals("REVERSE")) {
                        normale_volgorde = !normale_volgorde;
                    }
                } else {
                    input.nextLine();
                    System.out.println("Welke kleur? (Blue, Yellow, Green, Red)");
                    newColor = input.nextLine();
                    if (bovensteKaart.getIcoon().equals("+4")){
                        spelerNext.drawKaart(kaarten);
                        spelerNext.drawKaart(kaarten);
                        spelerNext.drawKaart(kaarten);
                        spelerNext.drawKaart(kaarten);
                        spelerNummerAanDeBeurt += 1;
                    }
                }
            } catch (IndexOutOfBoundsException exception){
                spelerAanDeBeurt.drawKaart(kaarten);
            } catch (NullPointerException | ArithmeticException exception){
                System.out.println("Er is een fout in de code. Gelieve een bug te reporten " +
                        "op Github met de volgende informatie:");
                throw exception;
            }
            spelerNummerAanDeBeurt++;
            Util.hide();
        }
    }
}
