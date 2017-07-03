def test_add_remove_products(app):
    app.open_popular()
    i = 1
    while i <= 3:
        app.add_product_to_cart(i)
        i += 1

    app.open_checkout()
    app.remove_products_from_cart()
    items_after_removal = app.check_cart_empty()
    assert items_after_removal == None










