import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        boolean normale_volgorde = false;
        int spelerAanDeBeurt = 0;
        Kaart[] kaarten = VoegKaartenToe.addKaarten(2, 2, 4);
        Scanner input = new Scanner(System.in);
        System.out.println("Hoeveel spelers?");
        Speler[] spelers = new Speler[input.nextInt()];
        for (int i = 0; i < spelers.length; i++) {
            spelers[i] = new Speler(i, kaarten);
        }
        while (Util.getWinner(spelers) != -1){

        }
    }
}
