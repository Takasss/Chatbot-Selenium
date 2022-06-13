from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

class WhatsappBot:

    def __init__(self):
        #Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["TestePy"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def AbrirWhats(self):
        #Abre o WhatsApp
        self.driver.get('https://web.whatsapp.com')
        sleep(20)

    def ProcuraPessoa(self):
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element(By.XPATH,
                f"//span[@title='{grupo_ou_pessoa}']")
            sleep(5)
            #Clica na pessoa
            campo_grupo.click()

    def Envia_msg(self, msg):
        """ Envia uma mensagem para a conversa aberta """
        try:
            sleep(2)
            # Seleciona a caixa de mensagem
            self.caixa_de_mensagem = self.driver.find_element(By.CLASS_NAME, 'p3_M1')
            # Digita a mensagem
            self.caixa_de_mensagem.send_keys(msg)
            sleep(2)
            # Seleciona botão enviar
            self.botao_enviar = self.driver.find_element(By.XPATH,
	            "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]/button")
            # Envia msg
            self.botao_enviar.click()
            sleep(2)
        except Exception as e:
            print("Erro ao enviar msg", e)

    def ultima_msg(self):
        """ Captura a ultima mensagem da conversa """
        try:
            sleep(2)
            texto = self.driver.find_element(By.XPATH,
                "//*[@id='pane-side']/div/div/div/div[11]/div/div/div[2]/div[2]/div[1]/span").text
            return texto
        except Exception as e:
            print("Erro ao ler msg, tentando novamente!")

    def msg_ativa(self):
        try:
            sleep(2)
            self.procurar_conversa = self.driver.find_element(By.XPATH,
	            "//*[@id='pane-side']/div/div/div/div[10]/div/div/div[2]/div[2]/div[2]/span[1]/div/span")
            self.procurar_conversa.click()
            sleep(2)
        except Exception as f:
            print("Erro ao ler novas conversas", f)




bot = WhatsappBot()
bot.AbrirWhats()
bot.ProcuraPessoa()
bot.Envia_msg("Olá, sou o bot do Whatsapp! Para receber ajuda digite: /help")
msg = ""
sleep(2)
while msg != "/quit":
    sleep(3)
    msg = bot.ultima_msg()
    sleep(2)
    if msg == "/help":
        bot.Envia_msg("Bot: Esse é um texto com os comandos válidos: /help (para ajuda) /mais (para saber mais) /quit (para sair)")
        sleep(2)
        bot.msg_ativa()
        sleep(2)
    elif msg == "/mais":
        bot.Envia_msg("Mais informações em breve.")
        sleep(2)
        bot.msg_ativa()
        sleep(2)
    elif msg == "/quit":
        bot.Envia_msg("Bye bye!")
        sleep(2)
        bot.msg_ativa()
        sleep(2)