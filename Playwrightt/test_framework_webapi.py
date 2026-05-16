import json
from urllib.parse import uses_relative

import pytest
from playwright.sync_api import Playwright, expect

from Playwrightt.pageobject.Dashboard import Dashboard
from Playwrightt.pageobject.login import Loginscreen
from Playwrightt.utils.apibase import APIUtils

with open("Playwrightt/data/credentials.json") as f:
    credentials = json.load(f)
    print(credentials)
    list_credentials=credentials["user_credentials"]

@pytest.mark.parametrize('user_credentials',list_credentials,indirect=True)
def test_e2e_web_api(playwright:Playwright ,browserInstance ,user_credentials):

    username = user_credentials["userEmail"]
    password = user_credentials["userPassword"]

    # create order by api
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright,user_credentials)

    # using ui we are logging
    login = Loginscreen(browserInstance)
    login.navigate()
    dashboarpage= login.login(username,password)

    orderpage =dashboarpage.selectordernavigationlink()
    historypage=orderpage.selectOrder(orderId)
    historypage.orderhistorypage()
    # context.close()

