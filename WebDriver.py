import requests
import urllib.request
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
WebDriver CLASS. abstracts selenium
'''
class WebDriver(object):

    '''
    init method. sets vars we are guna use. 
    '''
    def __init__(self):
        self.dna_url = 'https://faculty.ucr.edu/~mmaduro/random.htm'
        opts = webdriver.ChromeOptions()
        opts.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=opts)
        self.driver.get(self.dna_url)
        self.reset_button = "reset"
        self.textarea = "sequence"
        self.size_input = "size"

    '''
    abstraction of clicking reset, no need to know selenium
    '''
    def click_reset(self, button_name=""):
        if button_name == "":
            button_name = self.reset_button
        try:
            # first get new len
            length = self.GenerateSequenceSize()
            # enter val
            # print("length of input = " + str(length))
            size = self.driver.find_element_by_name(self.size_input)
            size.clear()
            size.send_keys(str(length))
            # print("length = " + self.driver.find_element_by_name(self.size_input) )
            # now hit reset
            self.driver.find_element_by_name(button_name).click()
            return True
        except Exception as e:
            print("we fucking DEAD")
            print(e)
            exit(2)

    '''
    abstraction of copying dna from webpage, no need to know selenium
    '''
    def get_textarea(self, textarea=""):
        if textarea == "":
            textarea = self.textarea
        try:
            return self.driver.find_element_by_name(textarea).get_attribute("value")
        except:
            raise Exception("oopsie woopsie we couldnt get the text!! :-( ")

    
    def GenerateSequenceSize(self,a=500,b=4000,n=3):
        # we need string size mod 3 == 0. this does dat
        if b-a < n:
            raise Exception('{} is too big'.format(n))
        result = random.randint(a, b)
        while result % n != 0:
            result = random.randint(a, b)
        return result
