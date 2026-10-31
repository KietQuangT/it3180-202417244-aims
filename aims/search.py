def search_by_title(cart, title):
    return [item for item in cart.items if title.lower() in item.title.lower()]
