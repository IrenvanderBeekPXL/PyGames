package board;

public class SpeciaalVak {
    String naam;
    private int euroBijTeTellen;
    private int beurenOverTeSlaan;
    private short plek;

    public SpeciaalVak(String naam, int euroBijTeTellen, int beurenOverTeSlaan, short plek) {
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

    public int getBeurenOverTeSlaan() {
        return beurenOverTeSlaan;
    }

    public short getPlek() {
        return plek;
    }
}
