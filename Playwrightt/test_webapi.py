from playwright.sync_api import Playwright, expect

from Playwrightt.utils.apibase import APIUtils



def test_e2e_web_api(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    # create order by api
    api_utils = APIUtils()
    orderid = api_utils.createOrder(playwright)

    # using ui we are logging
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill("mytestinggg1990@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Testing@123")
    page.get_by_role("button",name="Login").click()
    page.locator(".btn-custom").nth(1).click()
    # page.wait_for_timeout(5000)
    page.wait_for_load_state("networkidle")
    trcount = page.locator("tr").count()
    print(f"tr count",{trcount})
    print(f"order id is,{orderid}")
    for index in range(trcount):
        if page.locator("tr").nth(index).filter(has_text= orderid ).count() >0:
           print(f"order id is presented in table index ",{index},{orderid})
           page.locator("tr").nth(index).get_by_text("View").click()
           expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
           print(f" Order is view orders page")
           break
        else:
           print("order id is not presented n table")
