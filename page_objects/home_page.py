class HomePage():
    URL = "https://amazon.com"
    SEARCH_BOX = "twotabsearchtextbox"
    SEARCH_BTN = "nav-search-submit-button"

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.URL)

    def search_product(self, product):
        search_box = self.driver.find_element_by_id(self.SEARCH_BOX)
        search_box.send_keys(product);
        self.driver.find_element_by_id(self.SEARCH_BTN).click()
