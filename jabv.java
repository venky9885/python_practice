
import java.util.*;

public class jabv {
    // private static final int ArrayList = 0;

    public static void countFreq(int arr[], int n) {
        List<Integer> visted = new ArrayList<Integer>();
        ArrayList<Integer> freq = new ArrayList<Integer>();
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        // HashMap<String, String> capitalCities = new HashMap<>();

        for (int i = 0; i < n; i++) {
            if (!visted.contains(arr[i])) {
                int c = 0;
                for (int j = 0; j < n; j++) {
                    if (arr[i] == arr[j]) {
                        c += 1;
                    }
                }
                map.put(arr[i], c);
                freq.add(c);
                visted.add(arr[i]);
            }

            // System.out.println(arr[i]);
        }
        // List<Integer> t ;
        // t = Arrays.asList(visted);

        // List<Integer> ler = visted.Cast<Integer>().ToList();
        // Collections.reverse(visted);
        // Collections.sort(freq);
        System.out.println("****************************");
        System.out.println(visted);
        Collections.sort(visted);
        int index = Collections.binarySearch(visted, 10);
        System.out.println(index);

        System.out.println(map);
        for (var hr : map.entrySet()) {

            System.out.println(hr.getKey() + " " + map.get(hr.getKey()));

        }
        // for (int k = 0; k < visted.size(); k++) {
        // System.out.println(visted.get(k) + " " + freq.get(k));
        // }

    }

    public static void main(String[] args) {
        int arr[] = { 10, 5, 10, 15, 10, 5 };
        int n = arr.length;
        countFreq(arr, n);

        Scanner obj = new Scanner(System.in);

        String bc;
        double ab;
        Vector<String> v = new Vector<String>();
        List<String> al = new ArrayList<String>();
        ab = obj.nextDouble();
        // bc = obj.nextLine();
        bc = obj.nextLine();
        bc = obj.nextLine();

        // bc = obj.nextLine();
        al = Arrays.asList(bc.split(" "));
        v.addAll(al);
        Collections.sort(v);

        // v.spliterator(bc.split(" "));
        al.forEach(fd -> System.out.println(fd));
        v.forEach(fd -> System.out.println(fd));
        System.out.println();
        System.out.println(ab + " " + bc);
        obj.close();

        /*
         * LinkedList<String> linkedlist = new LinkedList<String>();
         * Stack<String> stk = new Stack<String>();
         * // Vector<Object> vector = new Vector<Object>();
         * Vector<Integer> vec = new Vector<>();
         * ArrayList<String> arraylist = new ArrayList<String>();
         * HashSet<String> hashset = new HashSet<String>();
         * HashMap<String, String> hashmap = new HashMap<String, String>();
         * TreeSet<String> treeset = new TreeSet<String>();
         * Queue<String> q1 = new PriorityQueue();
         * Queue<String> q2 = new ArrayDeque();
         * Deque<String> deque = new ArrayDeque<String>();
         * hashmap.put("0", "value");
         * hashmap.put("1", "value1");
         * hashmap.put("2", "value2");
         * System.out.println("Iterating Hashmap...");
         * System.out.println(hashmap.get("0"));
         * for (var m : hashmap.entrySet()) {
         * 
         * System.out.println(m.getKey() + " " + m.getValue());
         * }
         * arraylist.add("element");
         * arraylist.add("element1");
         * arraylist.set(1, "element3");
         * arraylist.forEach(action -> {
         * System.out.println(action);
         * });
         * ArrayList<String> newarrList = new ArrayList<String>();
         * newarrList = arraylist;
         * System.out.println(newarrList);
         * arraylist.clear();
         * System.out.println(arraylist);
         * vec.add(34);
         * vec.add(1);
         * Collections.sort(vec);
         * // vector.sort(c);
         * vec.forEach(act -> System.out.println(act));
         */
        // deque.add("a");

        // Iterator it = list.iterator();
        // while (it.hasNext()) {
        // System.out.println(it.next());
        // }
        // ArrayList<String> al = new ArrayList<String>();
        // al.add("455");
        // al.add("abg");
        // al.add("ebg");

        // Iterator itr = al.iterator();

        // while (itr.hasNext()) {
        // System.out.println(itr.next());
        // }

    }
}
/*
 * public class jabv {
 * public static void main(String[] args) {
 * 
 * char ch[] = { 'j', 'a', 'v', 'a', 't', 'p', 'o', 'i', 'n', 't' };
 * StringBuffer sb = new StringBuffer("Hello ");
 * // Method[] method = StringBuffer.class.getDeclaredMethod("append",
 * char.class);
 * System.out.println();
 * System.out.println(sb);
 * int a = 10;
 * String s = String.valueOf(a);
 * System.out.println("54" + a + "10" + s);
 * String s1 = new String(ch);
 * String s2 = "java 4558";
 * for (String i : s2.split(" ")) {
 * System.out.println(i);
 * }
 * 
 * System.out.println(s1.length());
 * System.out.println(s1.compareTo(s1));
 * s1 = s1.replace("av", "tv");
 * String s3 = s1.concat(s2);
 * System.out.println(s3);
 * System.out.println(s1.equals(s2));
 * System.out.println(s1.substring(2, s1.length() - 3));
 * System.out.println(s1.charAt(2));
 * System.out.println(s1.indexOf("v"));
 * System.out.println(s1.lastIndexOf("v"));
 * // System.out.println(s1.);
 * String nr = String.format("%d %s %f %.12f %c", 123, "abc", 3.14, 3.14, 'g');
 * String str2 = String.format("|%10f|", 101.12); // Specifying length of
 * integer
 * String str3 = String.format("|%10d|", 101);
 * System.out.println(str2 + "\n" + str3);
 * 
 * String sf1 = String.format("name is %s", s1);
 * String sf2 = String.format("value is %f", 32.33434);
 * String sf3 = String.format("value is %32.12f", 32.33434);// returns 12 char
 * fractional part filling with 0
 * 
 * System.out.println(sf1);
 * System.out.println(sf2);
 * System.out.println(sf3);
 * 
 * }
 * }
 * 
 */