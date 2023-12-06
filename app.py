import telebot
import time
import dados
import webbrowser
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constantes
site_url = "https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx"
bot = telebot.TeleBot(dados.chave_api)

# Funcoes
class Navegador:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless=new')
        prefs = {"download.default_directory": r"C:\Users\Nexxera\Downloads"}
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("prefs", prefs)
        service = ChromeService(log_path='chromedriver.log')
        self.driver = webdriver.Chrome(options=options, service=service)

    def inicializar(self):
        self.driver.get(site_url)
        self.driver.maximize_window()
        time.sleep(2)

    def buscar_numeros_sorteados(self):
        # self.aceitar_cookies()

        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Rejeitar'])[1]")))
            self.driver.find_element(By.XPATH, "(//button[normalize-space()='Rejeitar'])[1]").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//h2[1]//span[1]").location_once_scrolled_into_view
            time.sleep(1)
            resultado = self.driver.find_element(By.XPATH, "(//div[@class='resultado-loteria'])[1]").text
            print('')
            print(resultado)
            print('')
            premiacao = self.driver.find_element(By.XPATH, "(//div[@class='related-box gray-text no-margin'])[1]").text
            print(premiacao)
            print('')
            time.sleep(10)
            return resultado
        
        # Modifique o XPath abaixo para corresponder ao local onde os números sorteados estão na página
        # xpath_numeros_sorteados = "//div[@class='classe_do_elemento']//span[contains(@class, 'classe_do_numero')]"
        # numeros_sorteados_elementos = self.driver.find_elements(By.XPATH, xpath_numeros_sorteados)

        # # Converte os numeros sorteados para inteiros
        # numeros_sorteados = [int(elemento.text) for elemento in numeros_sorteados_elementos]

            # return numeros_sorteados
        except Exception as e:
            print(f"Erro {e}")

def gerar_palpites(numeros_sorteados):
    # Gera palpites com base nos numeros sorteados
    return list(numeros_sorteados)
mensagem = f'Olá, teste mega-sena python'

# Manipulador para encaminhar mensagens para um grupo
@bot.message_handler(func=lambda message: True)
def encaminhar_mensagem(message):
    # Substitua 'ID_DO_GRUPO' pelo ID real do seu grupo
    bot.polling()
    grupo_id = -100123456789  # Exemplo fictício, substitua pelo ID do seu grupo
    mensagem = message.text
    bot.send_message(grupo_id, f'Mensagem encaminhada: {mensagem}')
    

# Modulo principal
if __name__ == "__main__":
    # Inicializar o navegador
    navegador = Navegador()
    navegador.inicializar()

    # Buscar os numeros sorteados
    numeros_sorteados = navegador.buscar_numeros_sorteados()

    # Gerar palpites
    # palpites = gerar_palpites(numeros_sorteados)

    # Encaminhar palpites por telegran
    encaminhar_mensagem(numeros_sorteados)
    
    # encaminhar_palpites_por_whatsapp(palpites, contato)
