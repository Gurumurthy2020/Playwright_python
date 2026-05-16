import json

import pytest
from playwright.sync_api import Playwright

#  type 1
# {
#     "name": "John",
#     "age": 25,
#     "city": "New York"
# }
# print(f"json value ", val["name"], val["age"])

# {
#     "user": {
#         "firstName": "Rahul",
#         "lastName": "Shetty",
#         "address": {
#             "street": "MG Road",
#             "city": "Bangalore",
#             "pincode": 560001
#         }
#     }
# }
# print(f"first ", list["firstName"], list["address"]["street"])


# {
#     "employees": [
#         {"id": 1, "name": "Alice", "role": "QA"},
#         {"id": 2, "name": "Bob",   "role": "Dev"},
#         {"id": 3, "name": "Carol", "role": "BA"}
#     ]
# }
# print(f" employee details ", list[0]["name"], list[2]["role"])


# [
#     {"productName": "ZARA COAT", "price": 11500},
#     {"productName": "ADIDAS",    "price": 5000},
#     {"productName": "Nike",      "price": 7000}
# ]
# print(f"details ", val[0]["productName"])

# {
#     "company": "TechCorp",
#     "location": "Chennai",
#     "departments": [
#         {
#             "deptName": "Testing",
#             "employees": [
#                 {"name": "Guru",  "experience": 3},
#                 {"name": "Priya", "experience": 5}
#             ]
#         },
#         {
#             "deptName": "Development",
#             "employees": [
#                 {"name": "Raj",   "experience": 7},
#                 {"name": "Anita", "experience": 2}
#             ]
#         }
#     ]
# }
# print(f"details ", val["company"], "dept", val["departments"][0]["deptName"])
# print(f"name of first employee in first department", val["departments"][0]["employees"][0]["name"])
# print(f"experience of second employee in second department", val["departments"][1]["employees"][1]["experience"])
listusers=[""]
def test_validations_Json1(playwright:Playwright):
    with open("Playwrightt/data/type_json.json","r") as f:
        val=json.load(f)
        print(f"userEmail of second user",val["users"][1]["userEmail"])
        print(f"country in order",val["order"]["country"])
        print(f"loginSuccess message",val["messages"]["loginSuccess"])
        print(f"role of first user",val["users"][0]["role"])
        listusers=val["users"]


@pytest.mark.parametrize("users",listusers)
def test_parameter(playwright:Playwright,users):
    print("hi")