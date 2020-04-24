import java.util.List;

public class BinarySearch {
    private List<Integer> values;
    public BinarySearch(List<Integer> values) {
        this.values = values;
    }
    public int indexOf(int value) throws ValueNotFoundException  {
        int lo = 0;
        int hi = values.size()-1;
        while (lo <= hi) {
            int mid = lo + (hi - lo)/2;
            if      (values.get(mid) < value) lo = mid+1;
            else if (values.get(mid) > value) hi = mid-1;
            else    return mid;
        }
        throw new ValueNotFoundException("Value not in array");
    }
}
