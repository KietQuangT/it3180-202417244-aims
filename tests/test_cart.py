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
  
    def test_sort_cart(self):
        cart = Cart()
        dvd1 = DigitalVideoDisc("B Movie", "Drama", cost=15.0)
        dvd2 = DigitalVideoDisc("A Movie", "Action", cost=25.0)
        cart.add_dvd(dvd1)
        cart.add_dvd(dvd2)
        cart.sort_by_title()
        self.assertEqual(cart.items[0].title, "A Movie")
        cart.sort_by_cost()
        self.assertEqual(cart.items[0].cost, 25.0)
    def test_search_by_category(self):
        from aims.search import search_by_category
        dvd1 = DigitalVideoDisc("The Lion King", "Animation", cost=19.95)
        dvd2 = DigitalVideoDisc("Star Wars", "Sci-Fi", cost=24.95)
        res = search_by_category([dvd1, dvd2], "Animation")
        self.assertEqual(len(res), 1)
if __name__ == "__main__":
    unittest.main()