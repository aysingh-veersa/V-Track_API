import time
from tests.conftest import BaseTest
from tests.Keywords.Login import TestLogin
from tests.Profiles.UserProfle import VTrackCred
from tests.Utilities.TestActions import ObjectActions
from selenium.webdriver.common.by import By


class TestAPI(BaseTest):
    
    def test_API(self):
        TestLogin.login_into_application(self.driver, VTrackCred.username, VTrackCred.password)
        
        