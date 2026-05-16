from playwright.sync_api import Playwright

# orderspayload= {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}
orders_payload = {"orders":[{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]}
# orderLogin = {"userEmail": "mytestinggg1990@gmail.com", "userPassword": "Testing@123"}

class APIUtils:

    def gettoken(self,playwright:Playwright,abc):
        abc_username= abc["userEmail"]
        abc_password= abc["userPassword"]
        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com/",ignore_https_errors=True)
        response=api_request_context.post("/api/ecom/auth/login",
                                data={"userEmail": abc_username,"userPassword":abc_password},
)
        print(response.json())

        assert response.ok
        responseBody=response.json()
        return responseBody["token"]

    def createOrder(self,playwright:Playwright,abc):
        token=self.gettoken(playwright,abc)
        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com/",ignore_https_errors=True)
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=orders_payload,
                                 headers={"Authorization": token,
                                          "Content-Type": "application/json"})
        print(response.json())
        resp = response.json()
        resp_orders=resp["orders"][0]
        return resp_orders
