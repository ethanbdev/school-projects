//Ethan Borgen 
//April 7, 2016
//bloom filter - uses a bit array (array of ints, use the bits within the ints as 1 or 0) to check whether something is in the set 
//or definetly not in the set. In this case, it is being used as a basic spellchecker. Input a word, hash that word into a bit array
//hash table, then check it against a hashed list of words. Probability of a false positive: 0.001394. Requires line reader and txt file
//words.

public class BitArray {
    int M;
    int[] BitArray;
    public BitArray(int M) {
        this.M = M;
        if (M < 0) {
            throw new IllegalArgumentException("M is less than zero");
        }
        BitArray = new int[(M/32)+1];
        for (int j=0; j<(M/32)+1; j++) {
            BitArray[j] = 0;
        }
        
               
    }
    public boolean get(int n) {
        //Get the word corresponding to the hashed index
        if ((n < 0) || (n >= M)) {
            throw new IndexOutOfBoundsException("Index < 0 or Index > M");
        }
        int element;
        element = BitArray[(int) Math.floor(n/32)];
        int m =0;
        m = m | (1 << n % 32);
        int result = (element & m);
        return result != 0;
    }
    public void set(int n) {
        //set a bit array element to a word using the hashed index
        if ((n < 0) || (n >= M)) {
            throw new IndexOutOfBoundsException("Index < 0 or Index > M");
        }
        int m =0;
        m = m | (1 << n % 32);
        int element;
        element = BitArray[(int) Math.floor(n/32)];
        element = element | m;
        BitArray[(int) Math.floor(n/32)] = element;
    }
    
}

public class BloomFilter {
    int M;
    public BitArray bitArray;
    public BloomFilter(int M) {
        this.M = M;
        if (M < 0) {
            throw new IllegalArgumentException("M is less than zero.");
        }
        bitArray = new BitArray(M);
    }
  //hash functions. Hash the strings into a bit array index
    private int h1(String W) {
        int t =  W.hashCode();
        t = Math.abs(t) % M;
        return t;
    }
    private int h2(String W) {
        int t = 0;
        for (int j = 0; j < W.length(); j++) {
            t = (t << 1)^W.charAt(j);
        }
        return Math.abs(t) % M;
    }
    private int h3(String W) {
        int hashCode = 0;
        for (int i=0; i<W.length(); i++) {
            hashCode = (hashCode*51) + W.charAt(i);
        }
        return Math.abs(hashCode) % M;
    }
    private int h4(String W) {
        int intLength = W.length() / 4;
        long sum = 0;
        for (int j = 0; j < intLength; j++) {
            char c[] = W.substring(j * 4, (j * 4) + 4).toCharArray();
            long mult = 1;
            for (int k = 0; k < c.length; k++) {
                sum += c[k] * mult;
                mult *= 256;
            }
        }
        char c[] = W.substring(intLength * 4).toCharArray();
        long mult = 1;
        for (int k = 0; k < c.length; k++) {
            sum += c[k] * mult;
            mult *= 256;
        }
        int intsum = (int) sum;
        return Math.abs(intsum) % M;
    }
    private int h5(String W) {
        int code=1;
        for (int i=0; i<W.length(); i++) {
            code = code*W.charAt(i);
        }
        code = code*41;
        return Math.abs(code) % M;
    }
    public void add(String W) {
        //use the hash functions to add the words into the array
        int n = h1(W);
        bitArray.set(n);
        n = h2(W);
        bitArray.set(n);
        n = h3(W);
        bitArray.set(n);
        n = h4(W);
        bitArray.set(n);
        n = h5(W);
        bitArray.set(n);
    }
    public boolean isIn(String W) {
        // check if a word is in the set
        int n = h1(W);
        if (bitArray.get(n) == false) {
            return false;
        }
        n = h2(W);
        if (bitArray.get(n) == false) {
            return false;
        }
        n = h3(W);
        if (bitArray.get(n) == false) {
            return false;
        }
        n = h4(W);
        if (bitArray.get(n) == false) {
            return false;
        }
        n = h5(W);
        if (bitArray.get(n) == false) {
            return false;
        }
        else {
            return true;
        }
    }
    public double accuracy() {
        double p;
        p = (1.0-Math.pow(Math.E,(-5.0)*(850.0/M)));
        p = Math.pow(p, 5.0);
        return p;
    }
}

public class BloomFilter_Driver {
    public static void main(String [ ] args) {
        BloomFilter bitArray = new BloomFilter(13597);
        LineReader addLine = new LineReader(//<FILEPATH>);
        while (addLine.hasNext()) {
            String word = addLine.next();
            bitArray.add(word);
        }
        LineReader line = new LineReader(//<FILEPATH>);
        int count=1;
        while (line.hasNext()) {
            String word = line.next();
            if (bitArray.isIn(word) == false) {
                System.out.println(word);
                System.out.println(count);
                count = count+1;
            }
        }
        System.out.print("Probability of a false positive: ");
        System.out.printf("%.6f", bitArray.accuracy());
        System.out.println();
    }
}

// Output:
// Probability of a false positive: 0.001394