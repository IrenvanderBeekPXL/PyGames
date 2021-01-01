public class Kaart {
    private Soort soort;
    private Ranking ranking;

    public Kaart(Soort soort, Ranking ranking){
        this.soort = soort;
        this.ranking = ranking;
    }

    public Soort getSoort() {
        return soort;
    }

    public Ranking getRanking() {
        return ranking;
    }

    @Override
    public String toString() {
        return getSoort().getNaam() + " " + getRanking().getNaam();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Kaart)) return false;

        Kaart kaart = (Kaart) o;

        if (!getSoort().getNaam().equals(kaart.getSoort().getNaam())) return false;
        return getRanking().getNaam().equals((kaart.getRanking().getNaam()));
    }

    @Override
    public int hashCode() {
        int result = getSoort() != null ? getSoort().hashCode() : 0;
        result = 31 * result + (getRanking() != null ? getRanking().hashCode() : 0);
        return result;
    }
}
