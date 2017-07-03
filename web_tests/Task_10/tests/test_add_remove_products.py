import pytest
from web_tests.Task_10.app.application import Application

def test_add_remove_products(app):
    app.open_popular()
    i = 1
    while i <= 3:
        app.add_product_to_cart(i)
        i += 1





