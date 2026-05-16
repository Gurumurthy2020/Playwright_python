import page
from playwright.sync_api import Playwright, expect, Page


def test_uivalidationsDynamicscript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_role("textbox",name="username").fill("rahulshettyacademy")
    page.get_by_role("textbox",name="password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("button",name="Sign In").click()
    iphonelocator= page.locator("app-card").filter(has_text="iphone X")
    iphonelocator.get_by_role("button",name="Add ").click()
    page.wait_for_timeout(1000)

    nokialocator = page.locator("app-card").filter(has_text="Nokia Edge")
    nokialocator.get_by_role("button",name="Add ").click()
    page.wait_for_timeout(1000)
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_childwindowhandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newpage:
        page.locator(".blinkingText").filter(has_text="Free Access to InterviewQues/ResumeAssistance/Material").click()
        childpage=newpage.value
        expect(childpage.get_by_text("Documents request")).to_be_visible()
        text=childpage.locator(".red").text_content()
        # email = [w for w in text.split() if "@" in w]
        # print(email)
        words=text.split("at")
        print(words)
        email=words[1].strip().split(" ")[0]
        print(email)
        assert email == "mentor@rahulshettyacademy.com"
        childpage.close()
    page.locator(".form-control").nth(0).fill("username")
    page.wait_for_timeout(5000)


