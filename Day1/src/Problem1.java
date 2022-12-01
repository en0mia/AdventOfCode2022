import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

// Problem assignment: https://adventofcode.com/2022/day/1
public class Problem1 {
    public static void main(String[] args) throws IOException {
        int max = 0;
        int currentCalories = 0;
        final BufferedReader br = new BufferedReader(new FileReader(args[0]));
        String line = br.readLine();

        while (line != null) {
            if (line.equals("")) {
                if (currentCalories > max) {
                    max = currentCalories;
                }
                currentCalories = 0;
            } else {
                currentCalories += Integer.parseInt(line);;
            }
            line = br.readLine();
        }

        System.out.println("Result is: " + max);
    }
}