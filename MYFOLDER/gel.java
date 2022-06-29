
import java.util.*;
// import java.util.Collections;
// import java.util.List;
// import java.util.Scanner;

public class gel {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int tc = in.nextInt();
        int[] arr = new int[tc];
        for (int i = 0; i < tc; i++) {
            arr[i] = in.nextInt();
        }
        in.close();
        // for (int i = 0; i < tc; i++) {

        // }

        // sort odd places and even places in given array
        // int[] arr = { 1, 6, -1, 4, 0, 8, 5, 3, 9, 2 };

        int n = arr.length;
        List<Integer> odd = new ArrayList<Integer>();
        List<Integer> even = new ArrayList<Integer>();
        List<Integer> art = new ArrayList<Integer>();

        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                even.add(arr[i]);
            } else {
                odd.add(arr[i]);
            }
        }
        Collections.sort(odd);
        Collections.sort(even);
        int oi = 0, ei = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                art.add(even.get(ei));
                ei++;

            } else {
                art.add(odd.get(oi));
                oi++;

            }
        }
        System.out.println(art);
    }
}