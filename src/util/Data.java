package util;

public abstract class Data {
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

    public static boolean arrayIn (String[] array, String search){
        for (String i:array) {
            if (i.equals(search)){
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
}
