from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage():
    FIRST_RESULT_ITEM = '[data-image-index="1"]'
    QUANTITY_SELECT_DIV = 'selectQuantity'
    QUANTITY_SELECT_BTN = 'a-dropdown-prompt'
    QUANTITY_SELECT_OPTION = 'quantity_{}'
    PRODUCT_PRICE = 'price_inside_buybox'
    ADD_TO_CART_BTN = 'add-to-cart-button'

    def __init__(self, driver):
        self.driver = driver

    def select_first_product(self):
        self.driver.find_element_by_css_selector(self.FIRST_RESULT_ITEM).click()

    def select_product_quantity(self, quantity):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.QUANTITY_SELECT_DIV)))
        quantity_select_div = self.driver.find_element_by_id(self.QUANTITY_SELECT_DIV)
        quantity_select_div.find_element_by_class_name(self.QUANTITY_SELECT_BTN).click()
        self.driver.find_element_by_id(self.QUANTITY_SELECT_OPTION.format(int(quantity) - 1)).click()

    def get_product_price(self):
        return self.driver.find_element_by_id(self.PRODUCT_PRICE).text

    def add_product_to_cart(self):
        self.driver.find_element_by_id(self.ADD_TO_CART_BTN).click()
