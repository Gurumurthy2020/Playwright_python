from playwright.sync_api import Playwright, Page, expect


def test_morevalidations(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.locator("#hide-textbox").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

def test_alertshandling(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog",lambda dialog:dialog.accept())
    page.locator("#alertbtn").click()
    page.wait_for_timeout(5000)

def test_iframehandling(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    iframe=page.frame_locator("#courses-iframe")
    iframe.locator("(//a[contains(@class,'new-navbar-highlighter')])[1]").click()
    expect(iframe.locator("//h1[text()='All Access Subscription']")).to_contain_text("All Access Subscription")

def test_webtable(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    fruitename=page.locator("tr").filter(has_text="Strawberry")
    expect(fruitename.locator("td").nth("1")).to_have_text("23")

def test_dynamicwebtable(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    page.locator("select").nth(0).select_option("20")
    collvalue =0
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            collvalue=index
            print(f"coll value is {collvalue}")
            break

    row = page.locator("tbody tr")
    totalrowcount = row.count()
    rowvalue = 0
    print(f"total row count is {totalrowcount}")
    for index in range(totalrowcount):
        if row.nth(index).filter(has_text="Rice").count() > 0:
            rowvalue=index
            print(f"row  value is {rowvalue}")
            break
    Riceprice=row.nth(rowvalue).locator("td").nth(collvalue).inner_text()
    print(f"Rice price is {Riceprice}")

def test_mouseover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").click()
    page.get_by_role("link", name="Top").click()
    page.wait_for_timeout(5000)