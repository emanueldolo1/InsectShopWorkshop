from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class BlogPage(BasePage):

    slug = "/the-capsized-eight"
    shameless_link_locator = (By.LINK_TEXT, "Shameless")
    topic_label_locator = (By.CLASS_NAME, "__highlight")

    def navigate_to_page(self):
        self.navigate(self.slug)

    @property
    def shameless_link(self):
        return self.get_present_element(self.shameless_link_locator)

    @property
    def topic_label(self):
        return self.get_present_element(self.topic_label_locator)
