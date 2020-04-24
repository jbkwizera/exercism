import java.util.List;
import java.util.ArrayList;
class Sieve {
    private boolean[] isPrime;

    Sieve(int maxPrime) {
        isPrime = new boolean[maxPrime+1];
        for (int i = 2; i <= maxPrime; i++)
            isPrime[i] = true;

        for (int i = 2; i <= maxPrime; i++)
            if (isPrime[i])
                for (int j = i; j <= maxPrime/i; j++)
                    isPrime[i*j] = false;
    }

    List<Integer> getPrimes() {
        List<Integer> primes = new ArrayList<Integer>();
        for (int i = 2; i < isPrime.length; i++)
            if (isPrime[i]) primes.add(i);
        return primes;
    }
}
