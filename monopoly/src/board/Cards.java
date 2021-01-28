package board;

import java.util.ArrayList;

public class Cards {
    private String inhoud;
    private byte beurtenOverTeSlaan;
    private short gaNaarPos;
    private int euroBijTeTellen;
    public static ArrayList<Cards> kaarten = new ArrayList<>();

    public Cards(String inhoud, byte beurtenOverTeSlaan, short gaNaarPos, int euroBijTeTellen) {
        this.inhoud = inhoud;
        this.beurtenOverTeSlaan = beurtenOverTeSlaan;
        this.gaNaarPos = gaNaarPos;
        this.euroBijTeTellen = euroBijTeTellen;
        kaarten.add(this);
    }

    public String getInhoud() {
        return inhoud;
    }

    public byte getBeurtenOverTeSlaan() {
        return beurtenOverTeSlaan;
    }

    public short getGaNaarPos() {
        return gaNaarPos;
    }

    public int getEuroBijTeTellen() {
        return euroBijTeTellen;
    }
}
