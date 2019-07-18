from selenium.webdriver.support.select import Select


class ContactFormHelper:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver


    def submit_form(self):
        self.driver.find_element_by_id("wpforms-submit-145").click()


    def fill_in_description(self, description="This is a test message"):
        self.driver.find_element_by_id("wpforms-145-field_2").send_keys(description)


    def fill_in_email(self, email="pavlo@detesters.nl"):
        self.driver.find_element_by_id("wpforms-145-field_1").send_keys(email)
        self.driver.find_element_by_id("wpforms-145-field_2").click()
        self.driver.find_element_by_id("wpforms-145-field_2").clear()


    def select_topic(self, topic="Personal matter"):
        #TODO: topic should be enum
        self.driver.find_element_by_id("wpforms-145-field_3").click()
        Select(self.driver.find_element_by_id("wpforms-145-field_3")).select_by_visible_text(topic)
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='*'])[2]/following::option[4]").click()
        self.driver.find_element_by_id("wpforms-145-field_1").click()
        self.driver.find_element_by_id("wpforms-145-field_1").clear()


    def fill_in_surname(self, surname="Chigishev"):
        self.driver.find_element_by_id("wpforms-145-field_0-last").click()
        self.driver.find_element_by_id("wpforms-145-field_0-last").clear()
        self.driver.find_element_by_id("wpforms-145-field_0-last").send_keys(surname)


    def fill_in_first_name(self, name="Pavlo"):
        self.driver.find_element_by_id("wpforms-145-field_0").click()
        self.driver.find_element_by_id("wpforms-145-field_0").clear()
        self.driver.find_element_by_id("wpforms-145-field_0").send_keys(name)
