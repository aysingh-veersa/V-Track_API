from tests.Utilities.TestActions import ObjectActions
from tests.Pages.loginPage import LoginPage

class TestLogin:
    
    @staticmethod
    def login_into_application(self, username, password):
        ObjectActions.click_object(self, LoginPage.loginBtn)
        ObjectActions.switch_to_next_window(self)
        ObjectActions.set_text(self, LoginPage.username, username)
        ObjectActions.click_object(self, LoginPage.NextBtn)
        ObjectActions.set_text(self, LoginPage.password, password)
        