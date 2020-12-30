public enum Ranking {
    TWEE("2"), DRIE("3"), VieR("4"), VIJF("5"), ZES("6"), ZEVEN("7"), ACHT("8"),
    NEGEN("9"), TIEN("10"), BOER("Boer"), DAME("Dame"), KONING("Koning"), AAS("aas");
    private String naam;

    Ranking(String naam) {
        this.naam = naam;
    }

    public String getNaam() {
        return naam;
    }
}
