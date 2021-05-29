from behave import step

from page_objects.cart_page import CartPage
from page_objects.home_page import HomePage
from page_objects.search_results_page import SearchResultsPage


@step('I go to the amazon home page')
def go_to_home(context):
    context.home_page = HomePage(context.driver)
    context.home_page.go()


@step('I search for product "{product}"')
def search_product(context, product):
    context.home_page.search_product(product)
    context.search_results_page = SearchResultsPage(context.driver)


@step('I add the first item to the cart with quantity "{quantity}"')
def add_product_to_cart(context, quantity):
    context.search_results_page.select_first_product()
    context.search_results_page.select_product_quantity(quantity)

    context.product_price = float(context.search_results_page.get_product_price().split("$")[1])
    context.quantity = (quantity)

    context.search_results_page.add_product_to_cart()


@step('I open the cart')
def open_cart_page(context):
    context.home_page.go_to_cart_page()
    context.cart_page = CartPage(context.driver)


@step('I select "{quantity}" as quantity')
def select_quantity(context, quantity):
    context.cart_page.select_quantity(quantity)
    context.quantity = quantity


@step('I verify that the total price and quantity are correct')
def verify_total_price_and_quantity(context):
    assert context.cart_page.get_items_count() == int(context.quantity)
    assert float(context.cart_page.get_total_price()) == float(int(context.quantity) * context.product_price)

