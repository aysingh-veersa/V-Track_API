from tests.conftest import BaseTest
from tests.Keywords.Login import TestLogin
from tests.Profiles.UserProfle import VTrackCred
from tests.Utilities.TestActions import ObjectActions
from selenium.webdriver.common.by import By
import requests


class TestAPI(BaseTest):
    
    def test_API(self):
        TestLogin.login_into_application(self.driver, VTrackCred.username, VTrackCred.password)
        access_Token = ObjectActions.get_localStorage_Variable(self.driver, "accessToken")
        header = {
            'Accept': 'application/json, text/plain, */*',
            'Authorization': f'Bearer {access_Token}',
            'Origin': 'https://vtrack-dev-web.azurewebsites.net',
            'Referer': 'https://vtrack-dev-web.azurewebsites.net/',
        }
        response  = requests.get('https://vtrack-dev-api.azurewebsites.net/Client/get-clients?page=1&pagesize=10&sortBy=clientName&sortDir=ASC&searchKey=&timestamp=1709276135171',headers=header)
        print(response.status_code)
        print(response.json())
        
        