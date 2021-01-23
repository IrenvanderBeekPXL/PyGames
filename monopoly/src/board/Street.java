package board;

import errors.HouseAdditionFailedException;
import errors.NotEnoughMoneyException;
import errors.PlayerNotFoundException;
import player.Player;

import util.Data;

public class Street {
    private int prijs;
    private String naam;
    private short plek;
    private boolean hypotheek = false;
    private byte houses = 0;
    private final int huisPrijs;
    private Player eigenaar = null;


    public Street(int prijs, String naam, short plek, int huisPrijs){
        setNaam(naam);
        setPlek(plek);
        setPrijs(prijs);
        this.huisPrijs = huisPrijs;
    }

    public Street(short plek){
        setPlek(plek);
        huisPrijs = Integer.MAX_VALUE;
    }

    public int getPrijs() {
        return prijs;
    }

    public void setPrijs(int prijs) {
        this.prijs = Data.respectMin(0, prijs);
    }

    public String getNaam() {
        return naam;
    }

    public void setNaam(String naam) {
        this.naam = naam;
    }

    public short getPlek() {
        return plek;
    }

    public void setPlek(short plek) {
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

    public byte getHouses() {
        return houses;
    }

    public int getHuisPrijs() {
        return huisPrijs;
    }

    public Player getEigenaar() throws PlayerNotFoundException {
        if (eigenaar != null) {
            return eigenaar;
        } else {
            String msg = "Nobody bought this street yet";
            throw new PlayerNotFoundException(msg);
        }
    }

    public int buy(Player player) throws NotEnoughMoneyException {
        if (player.getMoney() < getPrijs()){
            String msg = "Player does not have money to buy this street";
            throw new NotEnoughMoneyException(msg);
        } else {
            eigenaar = player;
            return getPrijs();
        }
    }
}
