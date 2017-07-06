def test_add_remove_products(app):
    qtty = app.get_items_in_cart()

    for i in range(1, 3):
        app.add_product_to_cart(i)
        assert app.get_items_in_cart() == (qtty + i)

    app.remove_products_from_cart()
    assert app.get_items_in_cart() == 0












