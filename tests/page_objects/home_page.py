import time

from mains.driver_utils import DriverUtils
from mains.element_helper import ElementHelper
from mains import config_utils
from tests.locators import home_page_locators
from selenium.webdriver.common.keys import Keys

class HomePage:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(HomePage, cls).__new__(cls)
            cls.driver_utils = DriverUtils()
            cls.element_helper = ElementHelper()
            cls.config = config_utils.read_base_config_file()

        return cls.instance

    def open_app_home_page(self):
        if self.driver_utils.get_driver_object() is None:
            self.driver_utils.set_driver_object(self.driver_utils.create_driver())
        self.element_helper.set_driver_object()
        str_url = self.config['website_url']
        self.element_helper.navigate(str_url)

        assert self.element_helper.get_url().__contains__(str_url), \
                    "Failed to open application: " + str_url

    def search_for_product(self, product_name: str):

        self.element_helper.type(home_page_locators.input_search, product_name)
        self.element_helper.click(home_page_locators.button_search)
        self.element_helper.wait_for_element_displayed(home_page_locators.text_product_title)

    def verify_product_displayed_in_search_result(self, product_name: str):
        time.sleep(2)
        result = False
        list_elements = self.element_helper.get_element_list(home_page_locators.text_product_title)
        if list_elements.__len__() > 0:
            for element in list_elements:
                element_text = self.element_helper.get_element_text(element)
                if element_text.__contains__(product_name):
                    result = True
                    break

        assert result, "Failed to find product in the search results named: " + product_name

    def add_product_into_cart(self, product_name):
        result = False
        list_elements = self.element_helper.get_element_list(home_page_locators.text_product_title)
        list_prod_elements = self.element_helper.get_element_list(home_page_locators.link_product)
        if list_elements.__len__() > 0:
            for element in list_elements:
                element_text = self.element_helper.get_element_text(element)
                if element_text.__contains__(product_name):
                    index = list_elements.index(element)
                    self.element_helper.click(list_prod_elements[index])
                    self.element_helper.click(home_page_locators.btn_add_to_cart)
                    self.close_popup_if_displayed()
                    result = True
                    break

        assert result, "Failed to add product into cart named: " + product_name

    def close_popup_if_displayed(self):
        if self.element_helper.is_element_displayed(home_page_locators.overlay_popup):
            self.element_helper.action_type(Keys.ESCAPE)
            self.element_helper.wait_for_invisibility_of(home_page_locators.overlay_popup)

    def verify_product_in_shopping_cart(self, product_name):
        self.element_helper.click(home_page_locators.btn_mini_cart)
        self.element_helper.wait_for_element_displayed(home_page_locators.div_mini_cart)

        result = False
        list_product_titles = self.element_helper.get_element_list(home_page_locators.order_products_titles)
        if list_product_titles.__len__() > 0:
            for element in list_product_titles:
                element_text = self.element_helper.get_element_text(element)
                if element_text.__contains__(product_name):
                    result = True
                    break

        assert result, "Failed to find product into product cart named: " + product_name




