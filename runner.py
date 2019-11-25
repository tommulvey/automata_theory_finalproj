import requests
import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


dna_url = 'https://faculty.ucr.edu/~mmaduro/random.htm'
opts = webdriver.ChromeOptions()
opts.add_argument("headless")
driver = webdriver.Chrome(chrome_options=opts)
driver.get(dna_url)
#time.sleep(10)

element = driver.find_element_by_name("reset").click()
t = driver.find_element_by_name("sequence").get_attribute("value")
window_before = driver.window_handles[0]
print(t)