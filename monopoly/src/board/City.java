package board;

public class City {
    private Street[] straten;
    private String kleur;
    private String naam;

    public City(String kleur, String naam, Street... straten){
        this.straten = straten;
        this.kleur = kleur;
        this.naam = naam;
    }

    public Street[] getStraten() {
        return straten;
    }

    public String getKleur() {
        return kleur;
    }

    public String getNaam() {
        return naam;
    }
}
