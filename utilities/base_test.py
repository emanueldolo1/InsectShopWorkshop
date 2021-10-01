from unittest import TestCase
from utilities import driver_builder


class BaseTest(TestCase):
    def setUp(self):
        self.driver = driver_builder.build_driver()

    def tearDown(self):
        self.driver.quit()
