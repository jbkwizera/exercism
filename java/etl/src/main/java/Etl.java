import java.util.*;

class Etl {
    Map<String, Integer> transform(Map<Integer, List<String>> old) {
        Map<String, Integer> mp;
        mp = new HashMap<String, Integer>();

        for (Integer value: old.keySet())
            for (String letter: old.get(value))
                mp.put(letter.toLowerCase(), value);
        return mp;
    }
}
