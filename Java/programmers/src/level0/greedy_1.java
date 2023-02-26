package greedy;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

public class greedy_1 {
    public static int n ;
    public static ArrayList<Integer> arrayList = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();

        for (int i =0; i < n; i++){
            arrayList.add(scan.nextInt());
        }
        Collections.sort(arrayList);

        int result = 0;
        int count = 0;
        for(int i = 0; i < n; i++){
            count += 1;
            if(count >= arrayList.get(i)){
                result += 1;
                count = 0;
            }
        }
        System.out.println(result);
    }
}
