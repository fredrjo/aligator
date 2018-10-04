from models.grabber import Grabber
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from time import sleep
import requests
import re
import json
import datetime

class MinEnergiGrabber(Grabber):
    #locators
    _username = "txtUsername"
    _password = "txtPassword"
    _loginButton = "btnLogin"

    _url = 'http://192.168.0.110'
    driver = None
    #locatorTypes
    _usernameType = "ID"
    _passwordType = "ID"
    _LoginButtonType = "ID"

    def __init__(self):
        self.driver = webdriver.Chrome()


    def getType(locatorType):
        if locatorType == 'ID':
            return By.ID
        else:
            print('No such type defined')

    def login(self):
        self.driver.get(self._url)
