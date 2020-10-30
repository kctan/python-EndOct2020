from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#driver = webdriver.Firefox()
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
executor_url = driver.command_executor._url
session_id = driver.session_id

print(session_id)
print(executor_url)

messages = ["first message", "second message", "third message"]
for i in range(3):
    driver.get("https://api.whatsapp.com/send?phone=6591234567&text="+ messages[i])
    print(datetime.datetime.now())
    if i > 0:
        time.sleep(5)

    print(datetime.datetime.now())

    elem = driver.find_element_by_id("action-button")
    elem.send_keys(Keys.RETURN)

    # click on button
    driver.implicitly_wait(3) # seconds
    elem = driver.find_element_by_link_text("use WhatsApp Web")
    actions = ActionChains(driver)
    actions.click(elem)
    actions.perform()


    driver.implicitly_wait(10) # seconds
    #elem = driver.find_element_by_class_name("_2S1VP copyable-text selectable-text")
    elem = driver.find_element_by_css_selector(
        "#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text")
    elem.send_keys(Keys.RETURN)

    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        print("no alert")
    #time.sleep(2)
    #alert = driver.switch_to.alert
    #alert.dismiss()
    print("iteration: " + str(i))

'''
element_to_click = driver.find_element_by_id("alert")
	target = driver.find_element_by_id("div2")
	#Create the object for Action Chains
	actions = ActionChains(driver)
	actions.click(element_to_click)
	# perform the operation on the element
	actions.perform()
'''

'''
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
print(driver.page_source)
driver.close()
'''
