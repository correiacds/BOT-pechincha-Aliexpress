from msedge.selenium_tools import Edge, EdgeOptions
from time import sleep
import random

class AliexpressBot:
    def __init__(self):
        self.options = EdgeOptions()
        self.options.use_chromium = True
        self.options.executable_path = 'msedgedriver.exe'
        
        mobile_emulation = {
     "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
     "userAgent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.78"}
        self.options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.options.add_argument("--log-level=3")
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")
        #self.options.add_argument("--headless")
        self.driver = Edge(options = self.options)
        self.driver.set_window_size(375, 812)
        url = input('Digite a url para ser ajudado: \n')
        self.driver.get(url)
    
    def revelar(self):
        botao_revelar = self.driver.find_element_by_xpath('//*[@id="list"]/div/div[3]/div/div[5]/div/span')
        botao_revelar.click()

    def registrar(self):
        #botao_registrar = self.driver.find_element_by_xpath('//*[@id="root"]/ul/li[1]')
        #botao_registrar.click()

        #input_pass = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div[3]/input')

        #text_pass = "Ali"+str(random.randint(11111, 99999))+"Conta"+str(random.randint(11111, 99999))
        
        #input_email.send_keys(text_email)
        #input_pass.send_keys(text_pass)
        sleep(3)
        input("Pressione ENTER para continuar quando terminar de logar")

    def ajudar(self):
        botao_ajudar = self.driver.find_element_by_xpath('//*[@id="list"]/div/div[3]/div/div[5]/div/span')
        botao_ajudar.click()
        
quantidade = int(input('Digite quantas vezes quer ser ajudado: \n'))
contador = 0
while(contador < quantidade):
    bot = AliexpressBot()
    sleep(3)
    bot.revelar()
    sleep(3)
    bot.registrar()
    sleep(3)
    bot.ajudar()
    sleep(5)
    bot.close()
    contador = contador + 1;
