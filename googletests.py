import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        # Set up the Firefox driver using webdriver_manager
        self.driver = webdriver.Firefox(GeckoDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.google.com/")

    def tearDown(self):
        # Close the Firefox driver
        self.driver.quit()

    def test_google_search(self):
        # Find the search input field and enter a search query
        search_input = self.driver.find_element(By.NAME, "q")
        search_input.send_keys("Python unittest")

        # Find the search button and click it
        search_button = self.driver.find_element(By.NAME, "btnK")
        search_button.click()

        # Print the URL after clicking the search button
        print("Current URL:", self.driver.current_url)

        # Verify that search results are displayed
        result_stats = self.driver.find_element(By.ID, "resultStats")
        print("Result Stats Text:", result_stats.text)
        self.assertTrue(result_stats.is_displayed(), "Search results not displayed")

    def test_search_suggestion(self):
        # Find the search input field and enter a partial query
        search_input = self.driver.find_element(By.NAME, "q")
        search_input.send_keys("Python")

        # Verify that search suggestions are displayed
        search_suggestions = self.driver.find_elements(By.CLASS_NAME, "sbl1")
        self.assertTrue(len(search_suggestions) > 0, "Search suggestions not displayed")

    def test_empty_search(self):
        # Find the search button and click it without entering a query
        search_button = self.driver.find_element(By.NAME, "btnK")
        search_button.click()

        # Verify that the user is still on the Google homepage
        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://www.google.com/", "Search button redirected to a different page")

    def test_search_button_visibility(self):
        # Verify that the search button is visible on the page
        search_button = self.driver.find_element(By.NAME, "btnK")
        self.assertTrue(search_button.is_displayed(), "Search button not visible")

if __name__ == "__main__":
    # Define the test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(GoogleSearchTest)

    # Define the test runner with HtmlTestRunner
    output_path = r'C:\Users\Bogdan\Desktop\test_reports'  # Change to your desired output path
    report_name = 'TestReport.html'
    runner = HtmlTestRunner.HTMLTestRunner(output=output_path, report_title="Google Search Test Report")

    # Run the tests and generate the HTML test report
    runner.run(suite)
