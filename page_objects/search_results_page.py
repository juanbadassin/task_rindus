class SearchResultsPage():
    FIRST_RESULT_ITEM = '[data-image-index="1"]'

    def __init__(self, driver):
        self.driver = driver

    def select_first_product(self):
        self.driver.find_element_by_css_selector(self.FIRST_RESULT_ITEM).click()
