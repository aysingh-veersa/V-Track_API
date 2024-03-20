import time
from tests.Utilities.TestActions import ObjectActions
from tests.Pages.loginPage import LoginPage

class TestLogin:
    
    @staticmethod
    def login_into_application(self, username, password):
        ObjectActions.click_object(self, LoginPage.loginBtn)
        ObjectActions.switch_to_window_title(self, "Sign in to your account")
        ObjectActions.set_text(self, LoginPage.username, username)
        ObjectActions.click_object(self, LoginPage.NextBtn)
        ObjectActions.set_text(self, LoginPage.password, password)
        ObjectActions.click_object(self, LoginPage.SignIn)
        ObjectActions.click_object(self, LoginPage.BackBtn)
        # ObjectActions.close_window_title(self, "Sign in to your account")
        ObjectActions.switch_to_window_title(self, "Veersa Portal")
        # time.sleep(10)
        # self.implicitly_wait(2)
        ObjectActions.verify_element_is_not_present(self, LoginPage.loading)
        # time.sleep(1)
        ObjectActions.click_object(self, LoginPage.V_track)
        
        