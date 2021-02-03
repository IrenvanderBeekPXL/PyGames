import java.util.ArrayList;
import java.util.Random;

public abstract class Data {
    private static final Random random = new Random();
    public static int minMax(int min, int max, int value){
        if (value < min){
            value = min;
        } else if (value > max){
            value = max;
        }
        return value;
    }
    public static double minMax(double min, double max, double value){
        if (value < min){
            value = min;
        } else if (value > max){
            value = max;
        }
        return value;
    }

    public static boolean arrayIn (Kleur[] array, String search){
        for (Kleur i:array) {
            if (i.getKleurStr().equals(search)){
                return true;
            }
        }
        return false;
    }
    public static boolean arrayIn (int[] array, int search){
        for (int i:array) {
            if (i == search){
                return true;
            }
        }
        return false;
    }
    public static boolean arrayIn (double[] array, double search){
        for (double i:array) {
            if (i == search){
                return true;
            }
        }
        return false;
    }
    public static boolean arrayIn (char[] array, char search){
        for (char i:array) {
            if (i == search){
                return true;
            }
        }
        return false;
    }

    public static boolean stringIn(String str, char search){
        return arrayIn(str.toCharArray(), search);
    }

    public static double round(double numberToRound, double roundTo){
        return (int)Math.round(numberToRound / roundTo) * roundTo;
    }

    public static int respectMin(int min, int value){
        return minMax(min, Integer.MAX_VALUE, value);
    }
    public static double respectMin(double min, double value) {
        return minMax(min, Double.MAX_VALUE, value);
    }

    public static int searchForInArray(Object[] array, Object searchFor) {
        return searchForInArray(array, searchFor, 0);
    }

    public static int searchForInArray(Object[] array, Object searchFor, int startFrom) {
        for (int i = startFrom; i < array.length; i++) {
            if (array[i] == searchFor){
                return i;
            }
        }
        return -1;
    }

    public static int randomNumber(int min, int max){
        return random.nextInt(max - min + 1) + min;
    }

    public static void printArray(Object[] array){
        for (Object i : array) {
            System.out.println(i);
        }
    }

    public static void printArray(ArrayList<?> array){
        printArray(array.toArray());
    }
}
