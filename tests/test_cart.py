import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
	def test_add_dvd_until_full(self):
		cart = Cart()
		for i in range(20):
			self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", "Category", 10.0)))
		# Dia thu 21 phai tra ve False
		self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", "Category", 10.0)))


if __name__ == "__main__":
	unittest.main()