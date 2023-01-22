from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import csv
from login_info_model import LoginInfo


def interacting(secs: int):
    for i in range(secs):
        sleep(1)
        print(f"Seconds: {i}", flush=True)


def skip_not_now(browser):
    try:
        sleep(10)
        not_now = browser.find_element(
            By.XPATH, "//button[contains(text(), 'Not Now')]")
        not_now.click()
    except:
        print("Unable to skip! Please skip manually.")
        pass


def instagram_login(loginInfo: LoginInfo):

    browser = webdriver.Chrome(options=Options())

    print("Opening Instagram...")
    browser.get('https://www.instagram.com/')

    sleep(5)

    username_input = browser.find_element(By.NAME, "username")
    password_input = browser.find_element(By.NAME, "password")

    print("Logging in...")
    username_input.send_keys(loginInfo.get_username())
    password_input.send_keys(loginInfo.get_password())
    password_input.send_keys(Keys.RETURN)

    print("Logged in successfully!")

    # Skip : Save Your Login Info?
    print("Skipping : Save Your Login Info?")
    skip_not_now(browser)

    # Skip : Turn On Notifications?
    print("Skipping : Turn On Notifications?")
    skip_not_now(browser)

    isDone = False
    while not isDone:
        i = input(
            "Type (N or n) and hit 'ENTER' to exit and login with another account: ")
        if i == "N" or i == "n":
            isDone = True
        else:
            print("Invalid input. Try again.\n\n")


loginInfos = []

isPathValid = False
while not isPathValid:
    credsPath = input("Enter the path to your credentials file: ")
    try:
        with open(credsPath, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                username = row[0]
                password = row[1]

                loginInfos.append(LoginInfo(username, password))
        isPathValid = True
    except:
        print("Invalid path. Try again.\n\n")

if len(loginInfos) == 0:
    print("No credentials found. Exiting...")
    exit()
else:
    loginInfos = loginInfos[::-1]

    for loginInfo in loginInfos:
        print(f"Logging in with {loginInfo.get_username()}")
        instagram_login(loginInfo)

    print("\n\nAll accounts logged in successfully!\n\n")
