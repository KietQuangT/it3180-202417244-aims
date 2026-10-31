import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
	# Test 1: Giới hạn tối đa 20 đĩa DVD (Phần A)
	def test_add_dvd_until_full(self):
		cart = Cart()
		for i in range(20):
			self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", "Category", cost=10.0)))
		self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", "Category", cost=10.0)))

	# Test 2: Tính tiền sau khi giảm giá hợp lệ (Phần B)
	def test_apply_discount(self):
		cart = Cart()
		cart.add_dvd(DigitalVideoDisc("DVD 1", "Category", cost=100.0))
		self.assertEqual(cart.apply_discount(20), 80.0)

	# Test 3: Bắt lỗi khi nhập phần trăm giảm giá vượt quá 100 (Phần B)
	def test_apply_discount_invalid_percent(self):
		cart = Cart()
		with self.assertRaises(ValueError):
			cart.apply_discount(150)

	# Test 4: Tìm kiếm DVD theo tiêu đề (Lab 02)
	def test_search_by_title(self):
		cart = Cart()
		dvd1 = DigitalVideoDisc("The Matrix", "Action", cost=20.0)
		cart.add_dvd(dvd1)
		# Kiểm tra tìm thấy đĩa có trong giỏ và không tìm thấy đĩa không tồn tại
		self.assertTrue(any(item.title == "The Matrix" for item in cart.items))
		self.assertFalse(any(item.title == "Inception" for item in cart.items))


if __name__ == "__main__":
	unittest.main()