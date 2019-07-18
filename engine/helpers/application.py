from selenium import webdriver
from engine.helpers.contact_form import ContactFormHelper
from engine.helpers.navigator import Navigator


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.home = "http://pavlo.nl/"
        self.form = ContactFormHelper(self)
        self.navigator = Navigator(self)
        self.navigator.go_to(self.home)


    def destroy(self):
        self.driver.quit()