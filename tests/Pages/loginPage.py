from selenium.webdriver.common.by import By

class LoginPage:
    loginBtn = (By.XPATH, "//button[@class='loginBtn']")
    username = (By.XPATH, "//input[@type='email']")
    password = (By.XPATH, "//input[@type='password']")
    NextBtn = (By.XPATH, "//input[@type='submit']")
    