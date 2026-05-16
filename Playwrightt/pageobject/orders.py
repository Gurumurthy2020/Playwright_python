from playwright.sync_api import expect

from Playwrightt.pageobject import orderhistory
from Playwrightt.pageobject.orderhistory import orderhistoryScreen


class orders:

    def __init__(self, page):
        self.page = page

    def selectOrder(self,orderId):
        self.page.wait_for_load_state("networkidle")
        row = self.page.locator("tr").filter(has_text=orderId)
        row.get_by_role(role="button", name="View").click()
        historypage = orderhistoryScreen(self.page)
        return historypage

    def ordercount(self,orderId):
        trcount = self.page.locator("tr").count()
        self.page.wait_for_load_state("networkidle")
        trcount = self.page.locator("tr").count()
        print(f"tr count", {trcount})
        # print(f"order id is,{orderId}")
        for index in range(trcount):
            if self.page.locator("tr").nth(index).filter(has_text=orderId).count() > 0:
                print(f"order id is presented in table index ", {index}, {orderId})
                self.page.locator("tr").nth(index).get_by_text("View").click()
                expect(self.page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
                print(f" Order is view orders page")
                break
            else:
                print("order id is not presented n table")
