from Playwrightt.pageobject.orders import orders


class Dashboard:
    def __init__(self, page):
        self.page = page

    def selectordernavigationlink(self):
        self.page.locator(".btn-custom").nth(1).click()
        orderpage = orders(self.page)
        return orderpage


