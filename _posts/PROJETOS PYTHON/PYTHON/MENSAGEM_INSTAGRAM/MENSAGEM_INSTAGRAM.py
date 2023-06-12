#Importa as bibliotecas necessarias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

#Utiliza o chromedriver para abrir o instagram
chromedrive.path = 'C:/Users/thebl/Downloads/chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)

#Colocamos nosso usuario e senha para poder entrar no instagram
usuario = webdriver.find_element_by_name('username')
usuario.send.keys('raffaomoccelin')
senha = webdriver.find_element_by_name('password')
senha.send.keys('Rafael@@@281102')

button_login = webdriver.find_element_by_css_selector('')