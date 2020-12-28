package UNO;

public class Kaart {
    private static final String[] TOEGELATEN_KLEUREN = new String[]{"red", "green", "blue", "yellow", "black"};
    private static final String[] TOEGELATEN_ICONEN = new String[]{"0", "1","2", "3", "4", "5", "6", "7", "8", "9", "+2", "+4", "WILD", "REVERSE", "SKIP"};
    private String color;
    private String icoon;



    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getIcoon() {
        return icoon;
    }

    public void setIcoon(String icoon) {
        this.icoon = icoon;
    }
}
