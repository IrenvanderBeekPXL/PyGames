import java.util.Arrays;
import java.util.Collections;
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // ophalen en voorbereiden
        Soort[] soorten = Soort.values();
        Ranking[] ranken = Ranking.values();
        Kaart[] kaarten = new Kaart[soorten.length * ranken.length];
        Random random = new Random();
        Scanner input = new Scanner(System.in);

        // kaarten array vullen met elke mogelijke combinatie
        int index = 0;
        for (Soort i: soorten) {
            for (Ranking j: ranken) {
                kaarten[index] = new Kaart(i, j);
                index++;
            }
        }

        // main loop
        int kaartIndexSpeler = 0;
        int kaartIndexPC = 0;
        Kaart kaartSpeler;
        Kaart kaartPC;
        while (kaartIndexSpeler >= 0){
            // shuffelen
            Collections.shuffle(Arrays.asList(kaarten));

            // willikeurige kaart nemen
            kaartIndexPC = random.nextInt(52);

            // kaart vragen
            System.out.println("Welke kaart wil je nemen? (1-52) (0 om te stoppen)");
            kaartIndexSpeler = input.nextInt() - 1;
            if (kaartIndexSpeler >= 0){
                kaartIndexSpeler = Data.minMax(0, 51, kaartIndexSpeler);
            } else{
                break; // to prevent craches, sorry
            }

            // kaarten opvragen
            kaartPC = kaarten[kaartIndexPC];
            kaartSpeler = kaarten[kaartIndexSpeler];

            // vergelijken en printen
            if (kaartPC.getRanking().ordinal() < kaartSpeler.getRanking().ordinal()){
                System.out.println("Jij hebt gewonnen!");
            } else if (kaartPC.getRanking().ordinal() > kaartSpeler.getRanking().ordinal()){
                System.out.println("Ik heb gewonnen!");
            } else{
                System.out.println("We hebben gelijkgespeeld");
            }
            System.out.println();
        }
        System.out.println("Bedankt voor het spelen");
    }
}
