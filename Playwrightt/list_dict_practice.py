# ============================================================
#        PYTHON LIST & DICTIONARY PRACTICE PROGRAMS
# ============================================================
# Instructions:
# 1. Read each program carefully
# 2. Write your answer below each question
# 3. Run the file in PyCharm to check output
# ============================================================


# ============================================================
#                        LIST PROGRAMS
# ============================================================

# ------------------------------------------------------------
# Program 1 — Easy (List Basics)
# ------------------------------------------------------------
fruits = ["apple", "banana", "mango", "orange", "grapes", "kiwi"]

# 1. Print all fruits
# Your answer:print(fruits)

# 2. Print only first 3 fruits
# Your answer:print(fruits[0:3])

# 3. Print last 2 fruits
# Your answer:print(fruits[4:6])

# 4. Print total count
# Your answer:totalfruits=0
# for fruit in fruits:
#     if fruit != "":
#         totalfruits = totalfruits+1
# print(f"total count",totalfruits)
# print(len(fruits))

# 5. Check if "mango" is in list
# Your answer:is_available=True
# for fr in fruits:
#     if fr == "mango":
#         print(f"mango is in the list",is_available)
#         break
# second option: print("mango" in fruits)


# ------------------------------------------------------------
# Program 2 — Easy (List Operations)
# ------------------------------------------------------------
languages = ["java", "python", "javascript", "selenium", "playwright"]

# 1. Add "kotlin" to end of list
# Your answer:languages.append("kotlin")
# print(f"added",languages)

# 2. Add "kotlin" at index 1
# Your answer:languages.insert(0,"kotlin")
# print(languages)

# 3. Remove "java" from list
# Your answer:languages.remove("java")
# print(languages)

# 4. Sort list alphabetically
# Your answer:languages.sort()
# print(languages)

# 5. Print reversed list
# Your answer:languages.reverse()
# print(languages)


# ------------------------------------------------------------
# Program 3 — Medium (List Numbers)
# ------------------------------------------------------------
numbers = [10, 25, 30, 45, 50, 15, 60, 35, 20, 55]

# 1. Print sum of all numbers
# Your answer:print(sum(numbers))

# 2. Print average of all numbers
# Your answer:average = sum(numbers)/len(numbers)
# print(average)

# 3. Print largest number
# Your answer:highers=10
# for num in numbers:
#     if num > highers :
#         highers = num
# print(highers)

# 4. Print smallest number
# Your answer:smallest = 25
# for num in numbers:
#     if num < smallest :
#         smallest = num
# print(smallest)

# 5. Print all even numbers
# Your answer:numbers = [10, 25, 30, 45, 50, 15, 60, 35, 20, 55]
# evennumbers =[]
# for num in numbers:
#     if num % 2 ==0:
#         evennumbers.append(num)
# print(evennumbers)

# 6. Print all numbers greater than 30
# Your answer:num = 30
# numgrterthan30=[]
# for numb in numbers:
#     if numb > num :
#         numgrterthan30.append(numb)
# print(numgrterthan30)


# ------------------------------------------------------------
# Program 4 — Medium (List Duplicates)
# ------------------------------------------------------------
tools = ["selenium", "playwright", "appium",
         "selenium", "cypress", "playwright", "appium"]

# 1. Remove all duplicate values
# Your answer:tools = ["selenium", "playwright", "appium",
#          "selenium", "cypress", "playwright", "appium"]
# dup = []
# notdup = []
# for index in tools:
#     if index not in notdup:
#         notdup.append(index)
#     elif index in notdup:
#         dup.append(index)
# print(dup)
# print(notdup)

# 2. Print unique values only
# Your answer:tools = ["selenium", "playwright", "appium",
#          "selenium", "cypress", "playwright", "appium"]
# dup = []
# notdup = []
# for index in tools:
#     if index not in notdup:
#         notdup.append(index)
#     elif index in notdup:
#         dup.append(index)
# print(dup)
# print(notdup)

# 3. Count how many times "selenium" appears
# Your answer:
selcount=0
dup1=[]
for index in tools:
    if index == "selenium" :
        selcount = selcount + 1

print(selcount)
# 4. Find index of "playwright"
# Your answer:print(f"",tools.index("playwright"))

# 5. Replace "appium" with "cypress"
# # Your answer:
for position in range(len(tools)):
    if tools[position] == "appium":
        tools[position] = "cypress"
print(tools)

# ------------------------------------------------------------
# Program 5 — Medium (List Filtering)
# ------------------------------------------------------------
marks = [45, 78, 92, 35, 60, 48, 85, 55, 30, 70]

# 1. Print pass students (marks >= 50)
# Your answer:
for mark in marks:
    if mark >=50:
        print(f"pass students", {mark})

# 2. Print fail students (marks < 50)
# Your answer:for mark in marks:
#     if mark >=50:
#         print(f"pass students", {mark})
#     elif mark < 50:
#         print(f"fail students",{mark})

# 3. Print highest mark
# Your answer:
highest = 0
for mark in marks:
    if mark > highest:
        highest = mark
print(highest)

# 4. Print lowest mark
# Your answer:lowest =92
# for mark in marks:
#     if mark < lowest:
#         lowest = mark
# print(lowest)

# 5. Print average mark
# Your answer:total =0
#
# for mark in marks:
#     total = total + mark
# print(total)
# average = total/len(marks)
# print(average)

# 6. Count pass students
# Your answer:count =0
# for mark in marks:
#     if mark >50:
#         count = count+1
# print(count)

# 7. Count fail students
# Your answer:failcount=0
# for mark in marks:
#     if mark<50:
#         failcount = failcount + 1
# print(failcount)


# ------------------------------------------------------------
# Program 6 — Medium (List Strings)
# ------------------------------------------------------------
words = ["Playwright", "pytest", "selenium",
         "python", "Java", "API", "postman"]

# 1. Print all strings in UPPERCASE
# Your answer:

# 2. Print all strings in lowercase
# Your answer:

# 3. Print strings that start with "p"
# Your answer:

# 4. Print length of each string
# Your answer:

# 5. Print strings that have more than 5 characters
# Your answer:


# ------------------------------------------------------------
# Program 7 — Hard (List of Dictionaries)
# ------------------------------------------------------------
employees = [
    {"name": "Guru",  "city": "Chennai",   "salary": 60000, "role": "QA"},
    {"name": "Priya", "city": "Bangalore", "salary": 75000, "role": "Dev"},
    {"name": "Raj",   "city": "Chennai",   "salary": 45000, "role": "QA"},
    {"name": "Alice", "city": "Mumbai",    "salary": 80000, "role": "Dev"},
    {"name": "Bob",   "city": "Bangalore", "salary": 55000, "role": "QA"},
    {"name": "Carol", "city": "Chennai",   "salary": 90000, "role": "BA"}
]

# 1. Print names of all employees
# Your answer:

# 2. Print employees from "Chennai"
# Your answer:

# 3. Print employees with salary > 50000
# Your answer:

# 4. Print names of QA employees only
# Your answer:

# 5. Find employee with highest salary
# Your answer:

# 6. Find average salary
# Your answer:

# 7. Count employees in each city
# Your answer:


# ------------------------------------------------------------
# Program 8 — Hard (Test Results)
# ------------------------------------------------------------
test_results = [
    {"testName": "test_login",    "status": "PASSED", "duration": 2.5},
    {"testName": "test_search",   "status": "FAILED", "duration": 4.2},
    {"testName": "test_order",    "status": "PASSED", "duration": 3.8},
    {"testName": "test_payment",  "status": "FAILED", "duration": 1.9},
    {"testName": "test_logout",   "status": "PASSED", "duration": 2.1},
    {"testName": "test_register", "status": "PASSED", "duration": 5.0},
    {"testName": "test_profile",  "status": "FAILED", "duration": 3.2}
]

# 1. Print all PASSED tests
# Your answer:

# 2. Print all FAILED tests
# Your answer:

# 3. Count total PASSED and FAILED
# Your answer:

# 4. Print test names that took more than 3 seconds
# Your answer:

# 5. Find slowest test
# Your answer:

# 6. Find fastest test
# Your answer:

# 7. Print pass percentage
# Your answer:


# ============================================================
#                     DICTIONARY PROGRAMS
# ============================================================

# ------------------------------------------------------------
# Program 9 — Easy (Dictionary Basics)
# ------------------------------------------------------------
user = {
    "name": "Guru",
    "age": 28,
    "city": "Chennai",
    "email": "guru@gmail.com"
}

# 1. Print all keys
# Your answer:

# 2. Print all values
# Your answer:

# 3. Print name and email
# Your answer:

# 4. Add new key "phone" with value "9876543210"
# Your answer:

# 5. Update city to "Mumbai"
# Your answer:

# 6. Delete "age" from dictionary
# Your answer:

# 7. Check if "email" exists
# Your answer:


# ------------------------------------------------------------
# Program 10 — Easy (Config Dictionary)
# ------------------------------------------------------------
browser_config = {
    "browser": "chromium",
    "headless": False,
    "timeout": 30000,
    "baseUrl": "https://rahulshettyacademy.com"
}

# 1. Print browser name
# Your answer:

# 2. Check if headless is True or False
# Your answer:

# 3. Update timeout to 60000
# Your answer:

# 4. Add new key "viewport" with value "1920x1080"
# Your answer:

# 5. Print all configuration keys
# Your answer:

# 6. Print total number of configurations
# Your answer:


# ------------------------------------------------------------
# Program 11 — Medium (Nested Dictionary)
# ------------------------------------------------------------
person = {
    "firstName": "Guru",
    "lastName": "Murthi",
    "address": {
        "street": "MG Road",
        "city": "Chennai",
        "state": "TamilNadu",
        "pincode": 600001
    }
}

# 1. Print full name (firstName + lastName)
# Your answer:

# 2. Print city
# Your answer:

# 3. Print pincode
# Your answer:

# 4. Add "landmark" to address
# Your answer:

# 5. Update firstName to "Rahul"
# Your answer:

# 6. Print all address keys
# Your answer:


# ------------------------------------------------------------
# Program 12 — Medium (Dictionary Marks)
# ------------------------------------------------------------
student_marks = {
    "name": "Alice",
    "marks": {
        "python":     85,
        "selenium":   72,
        "playwright": 90,
        "java":       45,
        "api":        78
    }
}

# 1. Print total marks
# Your answer:

# 2. Print average marks
# Your answer:

# 3. Print subject with highest marks
# Your answer:

# 4. Print subject with lowest marks
# Your answer:

# 5. Print subjects where marks > 80
# Your answer:

# 6. Check if student passed all subjects (marks >= 50)
# Your answer:


# ------------------------------------------------------------
# Program 13 — Hard (Inventory)
# ------------------------------------------------------------
inventory = {
    "products": [
        {"name": "Laptop",  "price": 75000, "category": "Electronics", "stock": "In Stock"},
        {"name": "Phone",   "price": 25000, "category": "Electronics", "stock": "Out of Stock"},
        {"name": "Shirt",   "price": 1500,  "category": "Clothing",    "stock": "In Stock"},
        {"name": "Watch",   "price": 8000,  "category": "Accessories", "stock": "In Stock"},
        {"name": "Tablet",  "price": 35000, "category": "Electronics", "stock": "In Stock"},
        {"name": "Shoes",   "price": 3000,  "category": "Clothing",    "stock": "Out of Stock"}
    ]
}

# 1. Print all product names
# Your answer:

# 2. Print products with price < 10000
# Your answer:

# 3. Find most expensive product
# Your answer:

# 4. Find cheapest product
# Your answer:

# 5. Print products that are "In Stock"
# Your answer:

# 6. Calculate total value of all products
# Your answer:

# 7. Print products by category "Electronics"
# Your answer:


# ------------------------------------------------------------
# Program 14 — Hard (Playwright Config)
# ------------------------------------------------------------
test_config = {
    "browsers": ["chromium", "firefox"],
    "baseUrl": "https://rahulshettyacademy.com",
    "users": [
        {"email": "admin@gmail.com",  "password": "Pass1", "role": "admin"},
        {"email": "user1@gmail.com",  "password": "Pass2", "role": "user"},
        {"email": "admin2@gmail.com", "password": "Pass3", "role": "admin"}
    ],
    "products": [
        {"name": "ZARA COAT", "price": 11500},
        {"name": "ADIDAS",    "price": 5000},
        {"name": "Nike",      "price": 7000}
    ],
    "countries": ["India", "USA", "UK", "Australia"]
}

# 1. Print all browser names
# Your answer:

# 2. Print baseUrl
# Your answer:

# 3. Print email of valid user (first user)
# Your answer:

# 4. Print all product names
# Your answer:

# 5. Find product with highest price
# Your answer:

# 6. Print users with role "admin"
# Your answer:

# 7. Check if "chromium" is in browsers list
# Your answer:

# 8. Calculate total price of all products
# Your answer:

# 9. Print countries list
# Your answer:

# 10. Add new browser "webkit" to browsers list
# Your answer:


# ============================================================
# Difficulty Level:
# Program 1, 2      → List Basics       ⭐ Easy
# Program 3, 4      → List Operations   ⭐⭐ Medium
# Program 5, 6      → List Filtering    ⭐⭐ Medium
# Program 7, 8      → List of Dicts     ⭐⭐⭐ Hard
# Program 9, 10     → Dict Basics       ⭐ Easy
# Program 11, 12    → Nested Dict       ⭐⭐ Medium
# Program 13, 14    → Mixed Complex     ⭐⭐⭐ Hard
# ============================================================
