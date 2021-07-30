from selenium import webdriver
from keyboard import press_and_release
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

input('Pressione Enter após escanear o QRCode')

quantidade_envios = 1
msg = 'Esta é uma mensagem automatizada, ignore ela...'
imagem = 'C:\\Paluch_Python\\frente.jpg'
contatos = ['Oi', 'Fabi Vopen','Júnior Vopen' ]
cont = 0
for i in contatos:
    name = contatos[cont]
    cont = cont +1


    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    for i in range(quantidade_envios):
        time.sleep(2)
        driver.find_element_by_css_selector("span[data-icon='clip']").click()
        attach = driver.find_element_by_css_selector("input[type='file']")
        attach.send_keys(imagem)
        time.sleep(3)
        msg_box = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]')
        msg_box.send_keys(msg, Keys.ENTER)
