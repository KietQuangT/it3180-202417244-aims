def search_by_category(items, category):
    return [dvd for dvd in items if dvd.category.lower() == category.lower()]
def search_by_title(items, keyword):
    return [dvd for dvd in items if keyword in dvd.title]
def search_by_title(cart, title):
    return [item for item in cart.items if title.lower() in item.title.lower()]
