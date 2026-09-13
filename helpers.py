from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import logging

class Helper():

    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, url, new_window=False):
        try:
            if new_window:
                self.driver.execute_script(f"window.open('{url}');")
            else:
                self.driver.get(url)
                self.driver.maximize_window()
            logging.info(f'Opened page: {url}')
        except Exception as e:
            logging.error(f'Go to page failed: {e}')
            raise

    def find_and_click(self, loc, timeout=10):
        try:
            elem = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(loc))
            elem.click()
            logging.info(f'Clicked element: {loc}')
        except Exception as e:
            logging.error(f'Find and click failed for {loc}: {e}')
            raise

    def find_and_send_keys(self, loc, inp_text, timeout=10):
        try:
            elem = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(loc))
            elem.send_keys(inp_text)
            logging.info(f'Entered text into element: {loc}')
        except Exception as e:
            logging.error(f'Find and send keys failed for {loc}: {e}')
            raise

    def get_attribute(self, loc, attribute, timeout=10):
        try:
            elem = WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(loc))
            value = elem.get_attribute(attribute)
            logging.info(f'Got attribute {attribute} for element {loc}: {value}')
            return value
        except Exception as e:
            logging.error(f'Get attribute failed for {loc}: {e}')
            raise

    def get_text(self, loc, timeout=10):
        try:
            elem = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(loc))
            text = elem.text
            logging.info(f'Got text for element {loc}: {text}')
            return text
        except Exception as e:
            logging.error(f'Get text failed for {loc}: {e}')
            raise

    def switch_window(self, window_id=0):
        try:
            self.driver.switch_to.window(self.driver.window_handles[window_id])
            logging.info(f'Switched to window: {window_id}')
        except Exception as e:
            logging.error(f'Switch window failed: {e}')
            raise

    def accept_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            logging.info(f'Accepted alert with text: {alert_text}')
            return alert_text
        except Exception as e:
            logging.error(f'Accept alert failed: {e}')
            raise

    def append_text_to_file(self, file_path, text):
        try:
            with open(file_path, 'a+') as f:
                f.write(text + '\n')
            logging.info(f'Appended text to file {file_path}: {text}')
        except Exception as e:
            logging.error(f'Append text to file failed for {file_path}: {e}')
            raise
