import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        int e = Math.min(a, b);
        int f = Math.min(c, d);

        System.out.println(Math.min(e, f));
    }
}