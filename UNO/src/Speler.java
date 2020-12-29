import java.util.ArrayList;
import java.util.Random;

public class Speler {
    private ArrayList<Kaart> kaarten;
    private int spelerNummer;

    public Speler(int spelerNummer, Kaart[] kaartenStapel){
        this.spelerNummer = spelerNummer;
        deelKaart(kaartenStapel);
    }

    public void deelKaart(Kaart[] kaartenStapel){
        for (int i = 0; i < 7; i++) {
            drawKaart(kaartenStapel);
        }
    }

    public ArrayList<Kaart> getKaarten() {
        return kaarten;
    }

    public void setKaarten(ArrayList<Kaart> kaarten) {
        this.kaarten = kaarten;
    }

    public void addKaart(Kaart kaart){
        kaarten.add(kaart);
    }

    public int getSpelerNummer() {
        return spelerNummer;
    }

    public Kaart popKaart(int kaartIndex){
        Kaart kaart = kaarten.get(kaartIndex);
        kaarten.remove(kaartIndex);
        return kaart;
    }

    public void drawKaart(Kaart[] kaartenStapel){
        Random random = new Random();
        int index = random.nextInt(kaartenStapel.length);
        kaarten.add(kaartenStapel[index]);

    }
}
