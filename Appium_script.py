import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



desired_capabilities = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "platformVersion": "9.0",
        "automationName": 'uiautomator2'
        # "app": "C:\\Users\\mahar\\PycharmProjects\\Appium_selenium\\app_binaries\\Wikipedia-2.7.50401.apk",
    }

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
driver.implicitly_wait(30)
driver.find_element(AppiumBy.ACCESSIBILITY_ID , "Wikipedia").click()
driver.find_element(By.ID , "org.wikipedia:id/search_container").click()
e = driver.find_element(By.ID , "org.wikipedia:id/search_src_text")
e.send_keys("Emanuel")
time.sleep(2)
manu = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView[1]")
manu.click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID , "Navigate up").click()
time.sleep(2)



