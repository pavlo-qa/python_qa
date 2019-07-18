# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_happy_flow_case(self):
        '''
        Test method to check contacts form functionality
        :return:
        '''
        driver = self.driver
        self.go_to(driver, "http://pavlo.nl/")
        self.navigate_to_contacts_page(driver)
        self.fill_in_and_submit_form(driver)

    def fill_in_and_submit_form(self, driver):
        self.fill_in_first_name(driver)
        self.fill_in_surname(driver)
        self.select_topic(driver)
        self.fill_in_email(driver)
        self.fill_in_description(driver)
        self.submit_form(driver)

    def submit_form(self, driver):
        driver.find_element_by_id("wpforms-submit-145").click()

    def fill_in_description(self, driver):
        driver.find_element_by_id("wpforms-145-field_2").send_keys("This is a test message")

    def fill_in_email(self, driver):
        driver.find_element_by_id("wpforms-145-field_1").send_keys("pavlo@detesters.nl")
        driver.find_element_by_id("wpforms-145-field_2").click()
        driver.find_element_by_id("wpforms-145-field_2").clear()

    def select_topic(self, driver):
        driver.find_element_by_id("wpforms-145-field_3").click()
        Select(driver.find_element_by_id("wpforms-145-field_3")).select_by_visible_text("Personal matter")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='*'])[2]/following::option[4]").click()
        driver.find_element_by_id("wpforms-145-field_1").click()
        driver.find_element_by_id("wpforms-145-field_1").clear()

    def fill_in_surname(self, driver):
        driver.find_element_by_id("wpforms-145-field_0-last").click()
        driver.find_element_by_id("wpforms-145-field_0-last").clear()
        driver.find_element_by_id("wpforms-145-field_0-last").send_keys("Chigishev")

    def fill_in_first_name(self, driver):
        driver.find_element_by_id("wpforms-145-field_0").click()
        driver.find_element_by_id("wpforms-145-field_0").clear()
        driver.find_element_by_id("wpforms-145-field_0").send_keys("Pavlo")

    def navigate_to_contacts_page(self, driver):
        driver.find_element_by_id("menu-item-83").click()
        driver.find_element_by_link_text("Contacts").click()

    def go_to(self, driver, address):
        driver.get(address)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
