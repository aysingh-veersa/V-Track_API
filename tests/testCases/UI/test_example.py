from tests.conftest import BaseTest
from tests.Keywords.Login import TestLogin
from tests.Profiles.UserProfle import VTrackCred
import time
from tests.Utilities.TestActions import ObjectActions
from tests.Pages.loginPage import LoginPage
from selenium.webdriver.common.by import By
import requests


class TestUI(BaseTest):

    def test_ui(self):
        TestLogin.login_into_application(self.driver, VTrackCred.username, VTrackCred.password)
        time.sleep(10)
        ObjectActions.click_object(self.driver, LoginPage.clientTab)


