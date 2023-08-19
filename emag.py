import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class EmagSearchTest(unittest.TestCase):

    XPATH_SEARCH_RESULT = "/html/body/div[3]/div[2]/div/section[1]/div/div[3]/div[1]/div[1]/div[2]/div/div[2]/div[2]/a/div/div[2]/span"
    XPATH_SEARCH_RESULT2 = "/html/body/div[3]/div[2]/div/section[1]/div/div[3]/div[2]/div[1]/div[1]/div/span"

    def setUp(self):
        # Set up the Firefox WebDriver
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://emag.ro")

    def test_emag_search(self):
        # Find and interact with the search bar
        search_input = self.driver.find_element(By.XPATH, '//*[@id="searchboxTrigger"]')
        search_input.send_keys('monitoare')
        search_input.submit()

        # Wait for search results page to load
        self.driver.implicitly_wait(3)

        # Find the element and extract the text
        result_element = self.driver.find_element(By.XPATH, self.XPATH_SEARCH_RESULT)
        result_text = result_element.text

        # Extract the numeric part using regular expressions
        result_number = int(re.search(r'\d+', result_text).group())

        # Check if the numeric part is greater than 10
        self.assertTrue(result_number > 10, f"Number {result_number} is not greater than 10")

    def test_emag_inches_monitor(self):
        # Find and click the element for inches monitor
        search_input = self.driver.find_element(By.XPATH, '//*[@id="searchboxTrigger"]')
        search_input.send_keys('monitoare')
        search_input.submit()
        self.driver.implicitly_wait(3)

        inches_monitor_link = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/section[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/a[4]')
        inches_monitor_link.click()

        self.driver.implicitly_wait(3)

        # Find the element and extract the text
        result_element2 = self.driver.find_element(By.XPATH, self.XPATH_SEARCH_RESULT2)
        result_text2 = result_element2.text

        # Extract the numeric part using regular expressions
        result_number2 = int(re.search(r'\d+', result_text2).group())

        # Check if the numeric part is greater than 10
        self.assertTrue(result_number2 > 10, f"Number {result_number2} is not greater than 10")

        # You can perform further verifications or interactions on the loaded page if needed

    def test_emag_inches_monitor_ordoneaza_crecator(self):
            # Find and click the element for inches monitor
        search_input = self.driver.find_element(By.XPATH, '//*[@id="searchboxTrigger"]')
        search_input.send_keys('monitoare')
        search_input.submit()
        self.driver.implicitly_wait(10)

        inches_monitor_link = self.driver.find_element(By.XPATH,
                                                           '/html/body/div[3]/div[2]/div/section[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/a[4]')
        inches_monitor_link.click()



            # Click the specified button
        button = self.driver.find_element(By.XPATH,
                                              '/html/body/div[3]/div[2]/div/section[1]/div/div[3]/div[2]/div[1]/div[5]/div/div[2]/div[1]/button')
        button.click()

        time.sleep(2)

        button2 = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/section[1]/div/div[3]/div[2]/div[1]/div[5]/div/div[2]/div[1]/div/ul/li[3]/a')

        button2.click()
        time.sleep(3)




    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    # Create a test suite from the test case class
    test_suite = unittest.TestLoader().loadTestsFromTestCase(EmagSearchTest)

    # Create a test runner and set verbosity to 2 (for more detailed output)
    test_runner = unittest.TextTestRunner(verbosity=2)

    # Run the test suite and generate the report
    test_runner.run(test_suite)
