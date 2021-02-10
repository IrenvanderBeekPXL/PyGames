public enum Kleur {
    BLAUW("Blauw"), GEEL("Geel"), GROEN("Groen"), ORANJE("Oranje"),
    ROOD("Rood"), WIT("Wit"), ZWART("Zwart");

    private final String kleurStr;

    Kleur(String kleurStr) {
        this.kleurStr = kleurStr;
    }

    public String getKleurStr() {
        return kleurStr;
    }
}
