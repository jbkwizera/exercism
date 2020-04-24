import java.util.HashSet;
class IsogramChecker {
    boolean isIsogram(String phrase) {
        HashSet<Character> hs;
        hs = new HashSet<Character>();

        phrase = phrase.toLowerCase();
        for (int i = 0; i < phrase.length(); i++) {
            char c = phrase.charAt(i);
            if (Character.isLetter(c) && hs.contains(c))
                return false;
            hs.add(c);
        }
        return true;
    }
}
