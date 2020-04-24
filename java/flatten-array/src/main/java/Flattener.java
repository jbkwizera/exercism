import java.util.ArrayList;
import java.util.List;

class Flattener {
    List<Object> flatten(List<Object> list) {
        List<Object> res = new ArrayList<Object>();
        flatten(list, res);
        return res;
    }
    void flatten(List<Object> list, List<Object> res) {
        for (Object x: list)
            if (x instanceof List<?>) flatten((List<Object>)x, res);
            else if (x != null) res.add(x);
    }
}
