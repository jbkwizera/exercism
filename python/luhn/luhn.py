class Luhn:
    def __init__(self, card_num):
        self._card_num = card_num

    def valid(self):
        nonspace = []
        for ch in self._card_num:
            if ch != ' ':
                nonspace.append(ch)

        check_sum = 0
        N = len(nonspace)
        for i in range(N):
            if nonspace[N-i-1].isdigit():
                x = int(nonspace[N-i-1])
                if i % 2 == 1:
                    x = x*2 if x*2 < 10 else x*2-9
                check_sum += x
        return N > 1 and check_sum % 10 == 0
