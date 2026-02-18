import sys
from typing import Self

class Fraction:
	def __init__(self, num, den) -> None:
		if den == 0:
			raise ZeroDivisionError("Denominator can't be zero")
		elif den < 0:
			num = -num
			den = -den
		self.num = num
		self.den = den

	def __str__(self) -> str:
		return f"{self.num}/{self.den}"

	def __add__(self, other):
		result_num = (self.num * other.den) + (self.den * other.num)
		result_den = self.den * other.den
		common = gcd(result_num, result_den)
		return Fraction(result_num // common, result_den // common)


	def __mul__(self, other, /):
		result_num = self.num * other.num 
		result_den = self.den * other.den
		common = gcd(result_num, result_den)
		return Fraction(result_num // common, result_den // common)


	def __truediv__(self, other, /):
		result_num = self.num * other.den
		result_den = self.den * other.num
		common = gcd(result_num, result_den)
		return Fraction(result_num // common, result_den // common)


	def __sub__(self, other, /):
		result_num = (self.num * other.den) - (other.num * self.den)
		result_den = self.den * other.den
		common = gcd(result_num, result_den)
		return Fraction(result_num // common, result_den // common) 


	def __eq__(self, other, /) -> bool:
		self_num = self.num * other.den
		other_num = other.num * self.den
		return self_num == other_num


	def __lt__(self, other, /) -> bool:
		self_num = self.num * other.den
		other_num = other.num * self.den
		return self_num < other_num


	def __gt__(self, other, /) -> bool:
		self_num = self.num * other.den
		other_num = other.num * self.den
		return self_num > other_num


	def __ge__(self, other, /) -> bool:
		self_num = self.num * other.den
		other_num = other.num * self.den
		return self_num >= other_num

	def __le__(self, other, /) -> bool:
		self_num = self.num * other.den
		other_num = other.num * self.den
		return self_num <= other_num






def gcd(m,n):
	while n > 0:
		r = m
		m = n
		n = r % n
	return m

frac1 = Fraction(2,-6)
frac2 = Fraction(3,2)
frac3 = Fraction(2,2)
demo_addition = frac1 + frac2 + frac3
addition = frac1 + frac2
subtraction = frac1 - frac2
multiplication = frac1 * frac2
division = frac1 / frac2
gt = frac1 > frac2
lt = frac1 < frac2
ge = frac1 >= frac2
eq = frac1 == frac2
le = frac1 <= frac2 
print(f"Addition: {addition}\n subtraction: {subtraction}\nmultiplication: {multiplication}\ndivision: {division}\nGreater than: {gt}\nLess than: {lt}\nGe: {ge}\nLe: {le}\nEquals: {eq}")

# print(frac1)
# print(Fraction(1, -2) == Fraction(-1, 2))  # Should these be equal?
# print(Fraction(1, -2) > Fraction(0, 1))

# print(frac1, frac2)
# print(gcd(15,25))