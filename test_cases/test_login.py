import unittest
import HtmlTestRunner
from ddt import ddt, file_data
from selenium import webdriver
import sys
import os

sys.path.append("//home//norita//PycharmProjects//task")


class TestLogin(unittest.TestCase):

    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="//home//Descargas")

