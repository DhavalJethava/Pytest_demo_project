import os

import pytest
from pytest_bdd import scenario, given, when, then, parsers
from tests.page_objects.home_page import HomePage


@pytest.fixture()
def obj_home_page():
    return HomePage()


@scenario('..' + os.sep + 'features' + os.sep + 'goods_selection.feature',
          'Search for some goods and check if displayed in search result')
def test_goods_search():
    print('Search for some goods and check if displayed in search result')


@scenario('..' + os.sep + 'features' + os.sep + 'goods_selection.feature',
          'Select some goods and add to cart')
def test_add_to_cart():
    print('Select some goods and add to cart')


@given("User is on the application home page")
@when("User is on the application home page")
def open_app_home_page(obj_home_page):
    obj_home_page.open_app_home_page()


@when(parsers.cfparse('User search for the product "{product_name}"'))
def search_product(obj_home_page, product_name):
    obj_home_page.search_for_product(product_name)


@then(parsers.cfparse("User should see the product in the list '{product_name}'"))
def verify_product_displayed_in_search_result(obj_home_page, product_name):
    obj_home_page.verify_product_displayed_in_search_result(product_name)


@when(parsers.cfparse("User adds the product '{product_name}' into cart"))
def add_product_into_cart(obj_home_page, product_name):
    obj_home_page.add_product_into_cart(product_name)


@then(parsers.cfparse("User should see product '{product_name}' in the shopping cart"))
def verify_product_in_shopping_cart(obj_home_page, product_name):
    obj_home_page.verify_product_in_shopping_cart(product_name)
