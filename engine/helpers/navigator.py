


class Navigator():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver


    def navigate_to_contacts_page(self):
        self.driver.find_element_by_id("menu-item-83").click()
        self.driver.find_element_by_link_text("Contacts").click()


    def go_to(self, address="http://pavlo.nl/"):
        self.driver.get(address)
