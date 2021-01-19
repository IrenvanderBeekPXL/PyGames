public enum Kleur {
    WIT("Wit"), ROOD("Rood"), GROEN("Groen"), GEEL("Geel"),
    BLAUW("Blauw"), ZWART("Zwart"), ORANJE("Oranje");

    private final String kleurStr;

    Kleur(String kleurStr){
        this.kleurStr = kleurStr;
    }

    public String getKleurStr() {
        return kleurStr;
    }
}
