# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Rational: # En Python 2 debe incluirse la herencia de la clase object
    def __init__(self, num, den):
        self.numerator=num        
        self.denominator = den

    def add(self, other):
        newNumerator = self.numerator * other.denominator + self.denominator * other.numerator
        newDenominator = self.denominator * other.denominator
        return Rational(newNumerator, newDenominator)

    def __str__(self):
	return str(self.numerator)+"/"+str(self.denominator)


