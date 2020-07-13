// Provided Instructions:
// A pangram is a sentence that contains every single letter 
// of the alphabet at least once. For example, the sentence 
// "The quick brown fox jumps over the lazy dog" is a pangram, 
// because it uses the letters A-Z at least once (case is 
// irrelevant).
// 
// Given a string, detect whether or not it is a pangram. 
// Return True if it is, False if not. Ignore numbers and 
// punctuation.

import java.util.*;
import java.util.stream.Collectors;

public class Pangram {

    public boolean check1(String sentence) {
        // iterate through the string and collect characters as they appear
        List<Character> alphabet = new ArrayList<>();
        for (Character letter: String.join("",sentence.split("\\W|[0-9_]")).toCharArray()) {
            // add each char to alphabet array exactly once
            if (!alphabet.contains(Character.toLowerCase(letter))) {
                alphabet.add(Character.toLowerCase(letter));
            } 
        }
        // make sure the alphabet is in alphabetical order
        Collections.sort(alphabet);
        // create list of entire alphabet to test against
        List<Character> totalAlphabet = new ArrayList<>();
        for (int i = 97; i <= 122; i++) {
            totalAlphabet.add((char)i);
        }
        // return the result of the test
        return alphabet.equals(totalAlphabet);
    }

    // better version
    public boolean check(String sentence) {
        // to Pipeline stream
        return sentence.chars()
            .filter(c -> Character.isLetter(c))
            .mapToObj(c -> (char) Character.toLowerCase(c))
            .collect(Collectors.toSet())
            .size() == 26;
    }
    public static void main(String[] args) {
        String pangram1 = "The 1 quick brown fox jumps over the lazy dog.";
        String pangram2 = "You 1 shall not pass!";
        Pangram pg = new Pangram();
        System.out.println(pg.check(pangram1));
        System.out.println(pg.check(pangram2));
    }
}