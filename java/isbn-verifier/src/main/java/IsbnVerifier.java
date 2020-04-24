class IsbnVerifier {

    boolean isValid(String stringToVerify) {
        stringToVerify = stringToVerify.toLowerCase();
        String isbn = "";
        int sum = 0;
        int i = 10;
        for (char ch: stringToVerify.toCharArray()) {
            if (Character.isDigit(ch) || ch == 'x') {
                if (ch != 'x') sum += i*(ch - '0');
                else           sum += 10;
                i -= 1;
                isbn += ch;
            }
            else if (ch != '-') return false;
        }
        if (isbn.length() != 10) return false;
        return sum % 11 == 0;
    }
}
