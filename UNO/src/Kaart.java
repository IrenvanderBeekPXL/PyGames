public class Kaart {
    private static final String[] TOEGELATEN_KLEUREN = new String[]{"red", "green", "blue", "yellow", "black"};
    private static final String[] TOEGELATEN_ICONEN = new String[]{"0", "1","2", "3", "4", "5", "6",
            "7", "8", "9", "+2", "+4", "WILD", "REVERSE", "SKIP"};
    private String color;
    private String icoon;

    public Kaart(String color, String icoon){
        setColor(color);
        setIcoon(icoon);
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        if (Data.arrayIn(TOEGELATEN_KLEUREN, color)) {
            this.color = color;
        } else {
            System.out.println("Kleur bestaat niet");
        }
    }

    public String getIcoon() {
        return icoon;
    }

    public void setIcoon(String icoon) {
        if (Data.arrayIn(TOEGELATEN_ICONEN, icoon)) {
            this.icoon = icoon;
        } else {
            System.out.println("Icoon bestaat niet");
        }
    }

    @Override
    public String toString() {
        return getColor() + " " + getIcoon();
    }
}
