import time
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ObjectActions:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def click_object(driver, locator):
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(locator)).click()
        
    @staticmethod
    def set_text(driver, locator, text):
        # ObjectActions.clear_text(driver, locator)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)
        
    # @staticmethod
    # def clear_text(driver, locator):
    #     element = WebDriverWait(driver, 10).until(ec.visibility_of_element_located(locator)).click()
    #     element.send_keys(Keys.CONTROL, 'a')
    #     element.send_keys(Keys.BACKSPACE)
        
    @staticmethod
    def switch_to_window_title(driver, title):
        windows = driver.window_handles
        for window in windows:
            driver.switch_to.window(window)
            if driver.title == title:
                print('SWITCHED TO....' + driver.title)
                time.sleep(2)
                driver.maximize_window()
                break
    
    @staticmethod
    def close_window_title(driver, title):
        windows = driver.window_handles
        for window in windows:
            driver.switch_to.window(window)
            if driver.title == title:
                time.sleep(2)
                driver.close()
                break
            
    @staticmethod
    def switch_to_next_window(driver):
        next_window_index = (driver.window_handles.index(driver.current_window_handle)+1) % len(driver.window_handles)
        next_window_handle = driver.window_handles[next_window_index]
        driver.switch_to.window(next_window_handle)
        
        
