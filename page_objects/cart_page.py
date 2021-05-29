from time import sleep


class CartPage():
    ITEMS = 'sc-subtotal-label-activecart'
    PRICE = 'sc-subtotal-amount-activecart'
    PRODUCT_QUANTITY_SELECT = '[data-feature-id="sc-update-quantity-select"]'
    PRODUCT_QUANTITY_OPTION = '//a[text()="{}"]'

    def __init__(self, driver):
        self.driver = driver

    def get_items_count(self):
        label_text = self.driver.find_element_by_id(self.ITEMS).text
        return int(label_text.split("(")[1].split("item")[0])

    def get_total_price(self):
        price_text = self.driver.find_element_by_id(self.PRICE).text
        return price_text.split("$")[1]

    def select_quantity(self, quantity):
        self.driver.find_element_by_css_selector(self.PRODUCT_QUANTITY_SELECT).click()
        self.driver.find_element_by_xpath(self.PRODUCT_QUANTITY_OPTION.format(quantity)).click()
        sleep(1)
