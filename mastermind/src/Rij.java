public class Rij {
    private Kleur[] kleuren; // lengte 4
    private Boolean[] goed;

    public void setKleuren(Kleur... kleuren) {
        this.kleuren = kleuren;
        goed = new Boolean[kleuren.length];
    }

    public void check(Rij hoeHetMoet){
        Kleur[] kleurs = hoeHetMoet.kleuren;
        for (int j = 0; j < kleurs.length; j++) {
            Kleur i = kleurs[j];
            if (Data.arrayIn(kleuren, i.getKleurStr())) {
                goed[Data.searchForInArray(goed, null)] = kleuren[j].equals(i);
            }
        }
    }

    public String toString(){
        StringBuilder output = new StringBuilder();
        for (Kleur i : kleuren) {
            output.append(i.getKleurStr());
        }
        output.append(String.format("%n"));
        for (Boolean i : goed) {
            try {
                output.append(i);
            } catch (NullPointerException e){
                output.append("null");
            } finally {
                output.append(" ");
            }
        }
        return output.toString();
    }
}
