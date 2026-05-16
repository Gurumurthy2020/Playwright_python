from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright):
   browser = playwright.chromium.launch(headless=False)
   # context = browser.new_context()
   page = browser.new_page()
   page.goto("https://www.google.com")

def test_playwrightShortcut(page:Page):
    page.goto("https://www.google.com")

def test_rahulshettylogin(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learningss")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_orangeHrmLogin(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name="Login").click()
    page.get_by_role("link", name="Admin").click()
    page.locator("//div[contains(@class,'oxd-select-text-input')]").nth(0).click()
    page.get_by_role("option",name="Admin").click()

def test_firefoxlogin(playwright:Playwright):
    firefoxborwser = playwright.firefox.launch(headless=False)
    page = firefoxborwser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

def test_orangeHrmLvalidation(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name="Login").click()
    adminlink= page.locator(".oxd-main-menu-item--name").filter(has_text="Admin")
    adminlink.click()
    page.locator(".oxd-input--active").nth(1).fill("Admin")
    page.get_by_role("button",name=" Search ").click()
    expect(page.get_by_text("(1) Record Found")).to_be_visible()

