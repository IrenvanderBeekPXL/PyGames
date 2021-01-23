package board;

public class SpeciaalVak {
    private String naam;
    private int euroBijTeTellen;
    private byte beurenOverTeSlaan;
    private short plek;

    public SpeciaalVak(String naam, int euroBijTeTellen, byte beurenOverTeSlaan, short plek) {
        this.naam = naam;
        this.euroBijTeTellen = euroBijTeTellen;
        this.beurenOverTeSlaan = beurenOverTeSlaan;
        this.plek = plek;
    }

    public String getNaam() {
        return naam;
    }

    public int getEuroBijTeTellen() {
        return euroBijTeTellen;
    }

    public byte getBeurenOverTeSlaan() {
        return beurenOverTeSlaan;
    }

    public short getPlek() {
        return plek;
    }
}
