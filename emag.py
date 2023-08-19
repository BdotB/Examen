import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmagAutomation:


    COOKIES_ACCEPT_BUTTON = (By.XPATH, '/html/body/div[10]/div/div[2]/button[1]')



    def __init__(self, firefox_executable_path):
        # Set up Firefox WebDriver
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.binary_location = firefox_executable_path
        self.firefox = webdriver.Firefox(options=firefox_options)

    def navigate_to_website(self, url):
        self.firefox.get("https://www.emag.ro")
        self.firefox.maximize_window()

    def accept_cookies(self):
        accept_button = WebDriverWait(self.firefox, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/button"))
        )
        accept_button.click()

        inner_i_element = accept_button.find_element(By.TAG_NAME, "i")
        self.firefox.execute_script("arguments[0].scrollIntoView();", inner_i_element)
        inner_i_element.click()

        # Wait for the pop-up dialog to disappear
        WebDriverWait(self.firefox, 10).until_not(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div"))
        )

        print("Clicked the X button and closed the pop-up")

    def search_for_product(self, query):
        try:
            search_input = self.firefox.find_element(By.XPATH, '//*[@id="searchboxTrigger"]')

            search_input.send_keys('monitor')
            search_input.submit()

            print(f"Searched for 'monitor'")
        except Exception as e:
            print("Error:", e)

    def close_browser(self):
        time.sleep(5)
        self.firefox.quit()


if __name__ == "__main__":
    firefox_executable_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"  # Replace with the actual path
    emag_automation = EmagAutomation(firefox_executable_path)

    # Test 1: Apasare button x de la oferta zilei
    emag_automation.navigate_to_website("https://www.emag.ro/")

    emag_automation.accept_cookies()
    emag_automation.close_browser()

    # Test 2: Search for Monitoare
    emag_automation.navigate_to_website("https://www.emag.ro/")

    emag_automation.accept_cookies()
    emag_automation.search_for_product("monitoare")
    emag_automation.close_browser()
