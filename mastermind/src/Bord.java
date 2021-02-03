public class Bord {
    private Rij nodig;
    private Rij[] raadrijen;

    public Bord(Rij nodig, int aantalRaadMogelijkheden){
        raadrijen = new Rij[aantalRaadMogelijkheden];
        this.nodig = nodig;
    }

    public String addRij(Rij volgendeRij) throws NoSuchFieldException {
        try{
            raadrijen[Data.searchForInArray(raadrijen, null)] = volgendeRij;
        } catch (ArrayIndexOutOfBoundsException e) {
            throw new NoSuchFieldException();
        }
        volgendeRij.check(nodig);
        return volgendeRij.toString();
    }
}
