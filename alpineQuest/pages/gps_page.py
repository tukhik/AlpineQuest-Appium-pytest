from alpineQuest.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from alpineQuest.utils.constants import GPS_PAGE

switch_off_selector = (AppiumBy.XPATH, GPS_PAGE.SWITCH_OFF)
switch_on_selector = (AppiumBy.XPATH, GPS_PAGE.SWITCH_ON)
modal_title = (AppiumBy.XPATH, GPS_PAGE.MODAL_TITLE)

class PositioningPage(BasePage):

    def __init__(self, application):
        super().__init__(application)

    def open_app(self):
        return self.open_application()

    def find_gps_button(self):
        return self.find_button_by_image(GPS_PAGE.MENU_BUTTON_SELECTOR)

    def click_gps_button(self, coordinates):
        return self.click_button_at_coordinates(coordinates)

    def find_modal_title(self):
        return self.find(modal_title)
    
    def find_switch_location_button(self):
        return self.find(switch_off_selector)

    def find_element_by_xpath(self, xpath):
        return self.find((AppiumBy.XPATH, xpath))

    def find_and_click_location_gps_on_button(self):
        return self.find(switch_on_selector)
    
    def close_gps_modal(self):
        coordinates = self.find_button_by_image(GPS_PAGE.CLOSE_MODAL_ICON)
        return self.click_button_at_coordinates(coordinates)

    def wait_for_visible_element(self, element):
        return self.wait_element(element)

    def waite_until_modal_closed(self, element):
        return self.wait_element_is_not_visible(element)
    