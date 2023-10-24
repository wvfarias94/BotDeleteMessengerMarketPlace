
from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from selenium.webdriver.chrome.service import Service;
import time;
import pyautogui

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
email = 'INSIRA SEU EMAIL'
senha = 'SENHA'


#Acesso a pagina do marketplace
navegador.get("https://www.facebook.com/messages/t/6495585580523539")
pyautogui.click(1226,36,duration=1)
time.sleep(1)
navegador.find_element('xpath', '//*[@id="email"]').send_keys(email)
time.sleep(1)
navegador.find_element('xpath', '//*[@id="pass"]').send_keys(senha)
time.sleep(3)
navegador.find_element('xpath', '//*[@id="loginbutton"]').click()
time.sleep(5)

pyautogui.press('enter')

pyautogui.click(169,439,duration=2)
pyautogui.click(169,439,duration=2)
time.sleep(4)
for _ in range(50):
    
    pyautogui.click(353,325,duration=2)
    time.sleep(2)
    pyautogui.click(319,556,duration=2)
    time.sleep(2)
    pyautogui.click(1199,659,duration=2)
    time.sleep(2)


pyautogui.PAUSE


