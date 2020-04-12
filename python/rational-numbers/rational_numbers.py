from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        gcd        = self.gcd(numer, denom)
        self.numer = int(numer/gcd)
        self.denom = int(denom/gcd)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer*other.denom + other.numer*self.denom
        denom = self.denom*other.denom
        gcd   = self.gcd(numer, denom)
        return Rational(int(numer/gcd), int(denom/gcd))

    def __sub__(self, other):
        numer = self.numer*other.denom - other.numer*self.denom
        denom = self.denom*other.denom
        gcd   = self.gcd(numer, denom)
        return Rational(int(numer/gcd), int(denom/gcd))

    def __mul__(self, other):
        numer = self.numer*other.numer
        denom = self.denom*other.denom
        gcd   = self.gcd(numer, denom)
        return Rational(int(numer/gcd), int(denom/gcd))

    def __truediv__(self, other):
        numer = self.numer*other.denom
        denom = self.denom*other.numer
        gcd   = self.gcd(numer, denom)
        return Rational(int(numer/gcd), int(denom/gcd))

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power < 0:
            power = abs(power)
            return Rational(self.denom**power, self.numer**power)
        return Rational(self.numer**power, self.denom**power)

    def __rpow__(self, base):
        return base ** (self.numer/self.denom)

    def gcd(self, p, q):
        if q == 0:
            return p
        else:
            return self.gcd(q, p % q)
