package board;

import java.util.ArrayList;

public class AlgemeenKaart extends Cards{
    public static ArrayList<Cards> kaarten = new ArrayList<>();

    public AlgemeenKaart(String inhoud, byte beurtenOverTeSlaan, short gaNaarPos, int euroBijTeTellen) {
        super(inhoud, beurtenOverTeSlaan, gaNaarPos, euroBijTeTellen);
        kaarten.add(this);
    }

    public String getInhoud() {
        return super.getInhoud();
    }

    public byte getBeurtenOverTeSlaan() {
        return super.getBeurtenOverTeSlaan();
    }

    public short getGaNaarPos() {
        return super.getGaNaarPos();
    }

    public int getEuroBijTeTellen() {
        return super.getEuroBijTeTellen();
    }
}
