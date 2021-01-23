package board;

public class Street {
    int prijs;
    String naam;
    int plek;
    boolean hypotheek = false;

    public Street(int prijs, String naam, int plek){
        setNaam(naam);
        setPlek(plek);
        setPrijs(prijs);
    }

    public int getPrijs() {
        return prijs;
    }

    public void setPrijs(int prijs) {
        this.prijs = prijs;
    }

    public String getNaam() {
        return naam;
    }

    public void setNaam(String naam) {
        this.naam = naam;
    }

    public int getPlek() {
        return plek;
    }

    public void setPlek(int plek) {
        this.plek = plek;
    }

    public boolean isHypotheek() {
        return hypotheek;
    }

    public int setInHypotheek(){
        hypotheek = true;
        return getPrijs() / 2;
    }

    public int getOutOfHypotheek(){
        hypotheek = false;
        return getPrijs() / 2;
    }
}
