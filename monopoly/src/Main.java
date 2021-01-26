public class Main {
    public static void main(String[] args) {
        try {
            throw new Throwable();
        } catch (Throwable throwable) {
            throwable.printStackTrace();
        }
    }
}
