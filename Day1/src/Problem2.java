/*
    @author: Simone Nicol <en0mia.dev@gmail.com>
    @created: 01/12/22
    @copyright: Check the repository license.
*/

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Comparator;
import java.util.PriorityQueue;

// Problem assignment: https://adventofcode.com/2022/day/1
public class Problem2 {
    public static void main(String[] args) throws IOException {
        final PriorityQueue<Integer> queue = new PriorityQueue<>(11, Comparator.reverseOrder());
        int calories = 0;
        final BufferedReader br = new BufferedReader(new FileReader(args[0]));
        String line = br.readLine();

        while (line != null) {
            if (line.equals("")) {
                queue.add(calories);
                calories = 0;
            } else {
                calories += Integer.parseInt(line);
            }
            line = br.readLine();
        }

        int i = 0;
        int max = 0;

        while (!queue.isEmpty() && i < 3) {
            max += queue.poll();
            i++;
        }

        System.out.println("Result is: " + max);
    }
}
