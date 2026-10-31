import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
	def test_add_dvd_until_full(self):
		cart = Cart()
		for i in range(20):
			self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", "Category", 10.0)))
		self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", "Category", 10.0)))

	def test_apply_discount(self):
		cart = Cart()
		cart.add_dvd(DigitalVideoDisc("DVD 1", "Category",cost= 100.0))
		self.assertEqual(cart.apply_discount(20), 80.0)
		with self.assertRaises(ValueError):
			cart.apply_discount(150)


if __name__ == "__main__":
	unittest.main()