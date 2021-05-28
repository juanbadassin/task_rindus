from selenium import webdriver
import os
from configparser import ConfigParser


def before_all(context):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


def after_all(context):
    context.driver.close()
