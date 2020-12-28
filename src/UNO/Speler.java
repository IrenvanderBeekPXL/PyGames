package UNO;

import java.util.ArrayList;

public class Speler {
    private ArrayList<Kaart> kaarten;
    private int spelerNummer;

    public Speler(int spelerNummer, ArrayList<Kaart> kaarten){
        this.spelerNummer = spelerNummer;
        setKaarten(kaarten);
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
}
