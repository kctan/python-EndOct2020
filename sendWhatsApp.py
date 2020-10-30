from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

# construct the whatsapp message
# phone number
# message -- need to be urlencoded
message = "hello python course 101"
driver.get("https://api.whatsapp.com/send?phone=6591234567&text="+ message)

# click on send button
elem = driver.find_element_by_id("action-button")
elem.send_keys(Keys.RETURN)

# click on the use WhatsApp Link
driver.implicitly_wait(10) # seconds only need to call once, it will wait for 10 sec
elem = driver.find_element_by_link_text("use WhatsApp Web")
actions = ActionChains(driver)
actions.click(elem)
actions.perform()

# the selector can be found using 'right-click->Inspect' in Chrome browser
# In the copy the chrome developer window, right-click->copy->Copy Selector
#elem = driver.find_element_by_css_selector("#main > footer > div._3pkkz.V42si.copyable-area > div._1Plpp > div > div._2S1VP.copyable-text.selectable-text")
elem = driver.find_element_by_css_selector("#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text")

elem.send_keys(Keys.RETURN)

