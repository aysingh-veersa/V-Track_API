from tests.conftest import BaseTest
from tests.Keywords.Login import TestLogin
from tests.Profiles.UserProfle import VTrackCred


class TestAPI(BaseTest):
    
    def test_API(self):
        TestLogin.login_into_application(self.driver, VTrackCred.username, VTrackCred.password)
        