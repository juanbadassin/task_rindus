from time import sleep

from behave import step

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
def search_product(context, quantity):
    context.search_results_page.select_first_product()
    sleep(10000)
