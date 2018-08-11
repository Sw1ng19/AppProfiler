from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

def gesture_auth():
    cap = {
        "platformName": "iOS",
        "platformVersion": "11.4",
        "bundleId": "com.xxxx.insurance",
        "automationName": "XCUITest",
        "udid": "3e8325a7c0***************62bd4a7e",
        "deviceName": "iPhone"
    }

    host = "http://0.0.0.0:4723/wd/hub"
    driver = webdriver.Remote(host, cap)
    sleep(3)
    action = TouchAction(driver)
    start = driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="招商银行"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther\
                        /XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]')
    start_height = start.size['height']
    start_width = start.size['width']
    start_x = start.location['x']
    start_y = start.location['y']
    begin_x = start_x + start_width/2
    begin_y = start_y + start_height/2

    action.press(x=start_x, y=start_y).wait(100).move_to(x=start_x+start_width*2, y=begin_y).wait(100).move_to(x=start_x+start_width*2,y=start_y+start_height*2).wait(100).move_to(x=begin_x,y=start_y+start_height*2).perform().release()