package board;

import errors.HouseAdditionFailedException;

public class Street {
    private int prijs;
    private String naam;
    private int plek;
    private boolean hypotheek = false;
    private byte houses = 0;
    private final int huisPrijs;


    public Street(int prijs, String naam, int plek, int huisPrijs){
        setNaam(naam);
        setPlek(plek);
        setPrijs(prijs);
        this.huisPrijs = huisPrijs;
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

    public int addHuis() throws HouseAdditionFailedException {
        if (houses < 5){
            houses += 1;
            return huisPrijs;
        } else {
            String msg = "Too much houses to add one more";
            throw new HouseAdditionFailedException(msg);
        }
    }

    public int getHuurPrijs(){
        return getPrijs() / 20 + houses * (huisPrijs / 2);
    }
}
