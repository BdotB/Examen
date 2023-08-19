import re
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class EmagSearchTest(unittest.TestCase):

    XPATH_SEARCH_RESULT = "/html/body/div[3]/div[2]/div/section[1]/div/div[3]/div[1]/div[1]/div[2]/div/div[2]/div[2]/a/div/div[2]/span"

    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_emag_search(self):
        # Open the website
        self.driver.get("https://emag.ro")

        # Find and interact with the search bar
        search_input = self.driver.find_element(By.XPATH, '//*[@id="searchboxTrigger"]')
        search_input.send_keys('monitoare')
        search_input.submit()

        # Wait for search results page to load
        self.driver.implicitly_wait(10)

        # Find the element and extract the text
        result_element = self.driver.find_element(By.XPATH, self.XPATH_SEARCH_RESULT)
        result_text = result_element.text

        # Extract the numeric part using regular expressions
        result_number = int(re.search(r'\d+', result_text).group())

        # Check if the numeric part is greater than 10
        self.assertTrue(result_number > 10, f"Number {result_number} is not greater than 10")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
