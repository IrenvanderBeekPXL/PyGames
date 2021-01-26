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

    public SpeciaalVak(short plek){
        this(null, 0, (byte) 0, plek);
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

    @Override
    public boolean equals(Object o) {
        if (o == null) return false;
        if (this == o) return true;
        if (!(o instanceof SpeciaalVak)) return false;

        SpeciaalVak that = (SpeciaalVak) o;

        return getPlek() == that.getPlek();
    }

    @Override
    public int hashCode() {
        return getPlek();
    }
}
