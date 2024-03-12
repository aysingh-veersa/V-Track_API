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
        time.sleep(15)
        ObjectActions.switch_to_window_title(self.driver, "vTrack")
        time.sleep(10)
        if(ObjectActions.wait_for_element_to_be_clickable(self.driver, LoginPage.clientTab)):
            ObjectActions.click_object(self.driver, LoginPage.clientTab)
        time.sleep(5)
        ObjectActions.click_object(self.driver, LoginPage.addBtn)
        time.sleep(3)
        ObjectActions.set_text(self.driver, LoginPage.clientName,"Test")
        ObjectActions.click_object(self.driver, LoginPage.clientLocation)
        ObjectActions.click_object(self.driver, LoginPage.clientLocationLi)
        ObjectActions.click_object(self.driver, LoginPage.currency)
        ObjectActions.click_object(self.driver, LoginPage.inr)
        ObjectActions.click_object(self.driver, LoginPage.MSAStartDate)
        ObjectActions.set_text(self.driver, LoginPage.MSAStartDate,"03/12/2024")
        ObjectActions.click_object(self.driver, LoginPage.MSAEndDate)
        ObjectActions.set_text(self.driver, LoginPage.MSAEndDate,"03/13/2024")
        ObjectActions.click_object(self.driver, LoginPage.businessOwner)
        ObjectActions.click_object(self.driver, LoginPage.veersaDummyUser)
        ObjectActions.set_text(self.driver, LoginPage.paymentTerms,"1")
        ObjectActions.click_object(self.driver, LoginPage.deliveryOfficer)
        ObjectActions.click_object(self.driver, LoginPage.veersaDummyUser)
        ObjectActions.click_object(self.driver, LoginPage.addIcon)

        # ObjectActions.select_value_from_dropdown(self.driver, LoginPage.currency,"Indian Rupee")


