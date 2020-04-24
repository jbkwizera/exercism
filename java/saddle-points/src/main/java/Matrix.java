import java.util.List;
import java.util.Set;
import java.util.Collections;
import java.util.HashSet;

class Matrix {
    private List<List<Integer>> values;

    Matrix(List<List<Integer>> values) {
        this.values = values;
    }

    public Set<MatrixCoordinate> getSaddlePoints() {
        Set<MatrixCoordinate> set;
        set = new HashSet<MatrixCoordinate>();

        for (int i = 0; i < values.size(); i++)
            for (int j = 0; j < values.get(i).size(); j++)
                if (isColMin(i, j) && isRowMax(i, j))
                    set.add(new MatrixCoordinate(i+1, j+1));
        return set;
    }
    private boolean isColMin(int r, int c) {
        int min = values.get(r).get(c);
        for (int i = 0; i < values.size(); i++)
            if (values.get(i).get(c) < min)
                min = values.get(i).get(c);
        return min == values.get(r).get(c);
    }
    private boolean isRowMax(int r, int c) {
        int max = values.get(r).get(c);
        for (int j = 0; j < values.get(r).size(); j++)
            if (values.get(r).get(j) > max)
                max = values.get(r).get(j);
        return max == values.get(r).get(c);
    }
}
