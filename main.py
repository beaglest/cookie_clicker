import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


AWARDS = ["buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyFactory", "buyGrandma", "buyCursor"]


def return_int(s):

    z = s.split(",")
    y = "".join(z)
    m = int(y)
    return m


def get_reward(drv):

    for award in AWARDS:
        money1 = drv.find_element(By.ID, "money")
        a = drv.find_element(By.ID, award)
        c = a.get_attribute("class")
        x = a.text.split("\n")
        m1 = x[0].split("-")
 
        cost = return_int(m1[1])
        money = return_int(money1.text)

        if not c:
            if money > cost:
                print(a.text)
                try:
                    a.click()
                except selenium.common.exceptions.StaleElementReferenceException:
                    print("Stale problem\n")


        del a, c, x
    


driver = webdriver.Chrome()

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


start_time = time.time()

while (time.time() - start_time) < 300:
    cookie.click()
    if (5.0 - (time.time() - start_time) % 5.0) < 0.2:
        get_reward(driver)
