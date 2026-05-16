from dataclasses import replace
from itertools import count

fruits = ["apple", "banana", "mango", "orange", "grapes", "kiwi"]
print(fruits)
print(fruits[0:3])
print(fruits[4:6])
print(fruits[-2:])
print(len(fruits))
totalfruits=0
for fruit in fruits:
    if fruit != "":
        totalfruits = totalfruits+1
print(f"total count",totalfruits)

is_available=True
for fr in fruits:
    if fr == "mango":
        print(f"mango is in the list",is_available)
        break
print("mango" in fruits)

print(f"second programmmmmmmmmmmmmmmmmm")

languages = ["java", "python", "javascript", "selenium", "playwright"]
languages.append("kotlin")
print(f"added",languages)

languages.insert(1,"kotlin")
print(languages)

languages.remove("java")
print(languages)

languages.sort()
print(languages)

languages.reverse()
print(languages)

print(f"third  programmmmmmmmmmmmmmmmmm")

numbers = [10, 25, 30, 45, 50, 15, 60, 35, 20, 55]
total = 0
for num in numbers:
    total = total + num
print(total)

print(sum(numbers))

average = sum(numbers)/len(numbers)
print(average)

highers=numbers[0]
for num in numbers:
    if num > highers :
        highers = num
print(highers)

smallest = numbers[0]
for num in numbers:
    if num < smallest :
        smallest = num
print(smallest)

numbers = [10, 25, 30, 45, 50, 15, 60, 35, 20, 55]
evennumbers =[]
for num in numbers:
    if num % 2 ==0:
        evennumbers.append(num)
print(evennumbers)

num = 30
numgrterthan30=[]
for numb in numbers:
    if numb > num :
        numgrterthan30.append(numb)
print(numgrterthan30)

# [n for n in numbers if n % 2 == 0]


tools = ["selenium", "playwright", "appium",
         "selenium", "cypress", "playwright", "appium"]
dup = []
notdup = []
for index in tools:
    if index not in notdup:
        notdup.append(index)
    elif index in notdup:
        dup.append(index)
print(dup)
print(notdup)

selcount=0
dup1=[]
for index in tools:
    if index == "selenium" :
        selcount = selcount + 1

print(selcount)

print(f"",tools.index("playwright"))

print(tools)

for position in range(len(tools)):
    if tools[position] == "appium":
        tools[position] = "cypress"
print(tools)

marks = [45, 78, 92, 35, 60, 48, 85, 55, 30, 70]

for mark in marks:
    if mark >=50:
        print(f"pass students", {mark})
    elif mark < 50:
        print(f"fail students",{mark})
highest = marks[0]
for mark in marks:
    if mark > highest:
        highest = mark
print(highest)

lowest =marks[0]
for mark in marks:
    if mark < lowest:
        lowest = mark
print(lowest)

total =0

for mark in marks:
    total = total + mark
print(total)
average = total/len(marks)
print(average)

count =0
for mark in marks:
    if mark >=50:
        count = count+1
print(count)

failcount=0
for mark in marks:
    if mark<50:
        failcount = failcount + 1
print(failcount)
