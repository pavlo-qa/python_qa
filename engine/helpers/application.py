from selenium import webdriver
from selenium.webdriver.support.select import Select


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://pavlo.nl/"
        self.driver.get(self.base_url)

    def submit_form(self):
        driver = self.driver
        driver.find_element_by_id("wpforms-submit-145").click()

    def fill_in_description(self, description="This is a test message"):
        driver = self.driver
        driver.find_element_by_id("wpforms-145-field_2").send_keys(description)

    def fill_in_email(self, email="pavlo@detesters.nl"):
        driver = self.driver
        driver.find_element_by_id("wpforms-145-field_1").send_keys(email)
        driver.find_element_by_id("wpforms-145-field_2").click()
        driver.find_element_by_id("wpforms-145-field_2").clear()

    def select_topic(self, topic="Personal matter"):
        #TODO: topic should be enum
        driver = self.driver
        driver.find_element_by_id("wpforms-145-field_3").click()
        Select(driver.find_element_by_id("wpforms-145-field_3")).select_by_visible_text(topic)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='*'])[2]/following::option[4]").click()
        driver.find_element_by_id("wpforms-145-field_1").click()
        driver.find_element_by_id("wpforms-145-field_1").clear()

    def fill_in_surname(self, surname="Chigishev"):
        driver = self.driver
        driver.find_element_by_id("wpforms-145-field_0-last").click()
        driver.find_element_by_id("wpforms-145-field_0-last").clear()
        driver.find_element_by_id("wpforms-145-field_0-last").send_keys(surname)

    def fill_in_first_name(self, name="Pavlo"):
        driver = self.driver
        driver.find_element_by_id("wpforms-145-field_0").click()
        driver.find_element_by_id("wpforms-145-field_0").clear()
        driver.find_element_by_id("wpforms-145-field_0").send_keys(name)

    def navigate_to_contacts_page(self):
        driver = self.driver
        driver.find_element_by_id("menu-item-83").click()
        driver.find_element_by_link_text("Contacts").click()

    def go_to(self, address="http://pavlo.nl/"):
        driver = self.driver
        driver.get(address)

    def destroy(self):
        self.driver.quit()