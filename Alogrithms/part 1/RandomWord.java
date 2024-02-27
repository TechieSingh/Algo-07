import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        String champion = ""; // The current champion word
        int count = 0; // Number of words read so far

        while (!StdIn.isEmpty()) {
            String word = StdIn.readString();
            count++;

            // Select the word with probability 1/count to be the champion
            if (StdRandom.bernoulli(1.0 / count)) {
                champion = word;
            }
        }

        StdOut.println(champion); // Print the surviving champion word
    }
}
