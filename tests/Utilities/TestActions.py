import time
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ObjectActions:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def click_object(driver, locator):
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(locator)).click()
        
    @staticmethod
    def set_text(driver, locator, text):
        # ObjectActions.clear_text(driver, locator)
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(locator)).send_keys(text)
        
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
        window_handles = driver.window_handles
        global current_window_handle
        current_window_handle = driver.current_window_handle
        next_window_index = (window_handles.index(current_window_handle) + 1) % len(window_handles)
        next_window_handle = window_handles[next_window_index]
        driver.switch_to.window(next_window_handle)
     
    @staticmethod    
    def switch_to_current_window(driver):
        driver.switch_to.window(current_window_handle)
        
    @staticmethod
    def get_localStorage_Variable(driver, key):
        return driver.execute_script(f"return window.localStorage.getItem('{key}');")
        
        
    @staticmethod
    def wait_for_element_to_be_clickable(driver, locator):
        element = WebDriverWait(driver, 15).until(ec.element_to_be_clickable(locator))
        return bool(element)
    
    @staticmethod
    def switch_to_nextTab(driver, locator):
        element = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(locator))
        element.send_keys(Keys.CONTROL + 't')
        
        
        
