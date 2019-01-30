import time
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\simon.farren\\Downloads\\chromedriver.exe")  # Optional argument, if not specified will search path.
driver.get('https://soundcloud.com/biffyclyro/picture-a-knife-fight');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('Biffy Clyro')
search_box.submit()
#time.sleep(10) # Let the user actually see something!
#driver.quit()
