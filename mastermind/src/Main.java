import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Rij rijNeeded = new Rij();
        Kleur[] activeRij = new Kleur[4];
        for (int i = 0; i < 4; i++) {
            activeRij[i] = Kleur.values()[Data.randomNumber(0, Kleur.values().length - 1)];
        }
        Bord bord = new Bord(new Rij(activeRij.clone()), 10);
    }
}
