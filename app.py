# Importando base das funcionalidades selenium
import sys  # Biblioteca para recursos de identificacao de sistema operacional
import os  # Biblioteca para uso de recursos do sistema
import time  # Biblioteca para uso de sleep aguardar periodos de pausa
import logging  # Usado para desativar o log do webdriver-manager
# import shutil  # Usado para mover arquivos entre diretorios
import unicodedata  # Usado para remover acentuacao de strings
from logging.handlers import RotatingFileHandler  # Biblioteca utilizada para rotatividade de arquivos de log
from locale import setlocale, LC_ALL
from selenium import webdriver  # Importando WebDriver do Selenium
from selenium.webdriver.chrome.service import Service as ChromeService  # Importando o servico webdriver do selenium e definando o nome para o servico no chrome
from selenium.webdriver.firefox.service import Service as FirefoxService  # Importando o servico webdriver do selenium e definando o nome para o servico no firefox
from selenium.webdriver.common.by import By  # Recurso do Selenium Find POR
from selenium.webdriver.common.keys import Keys  # Recurso do Selenium uso de padroes de teclas ex Enter
from selenium.webdriver.common.action_chains import ActionChains  # Recursos do Selenium para acoes do mouse
from selenium.webdriver.support import expected_conditions as EC  # Recurso do Selenium como EC
from selenium.webdriver.support.ui import WebDriverWait  # Recurso do Selenium Usar para aguardar elementos aparecerem
import urllib3  # Biblioteca para desativar verificacao de ssl nao verificado googleapis

site1 = "https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx"

# Criar funcao para iniciar o navegador.
def inicializa_navegador(self):
    urllib3.disable_warnings()  # Desativando aviso de ssl nao verificado, pois, sao sistemas internos.
    os.environ['WDM_SSL_VERIFY'] = '0'  # Definindo para zero devido a erro de SSL auto assinado, removendo a verificacao
    logging.getLogger('WDM').setLevel(logging.NOTSET)  # Desabilitando o log do wdm webdriver-manager (Pode ser descomentado a qualquer momento)
    os.environ['WDM_LOG'] = '0'  # Desabilitando o log do wdm webdriver-manager (Pode ser descomentado a qualquer momento)
    os.environ['WDM_PRINT_FIRST_LINE'] = 'False'  # Desabilitando a insercao de linhas em branco no log do webdriver-manager
    
    try:
        retorno_nav = 'Google Chrome'
        if retorno_nav == "ERRO":
            ...
        elif retorno_nav == "Google Chrome":
            options = webdriver.ChromeOptions()  # Definindo opcoes para o webdriver para o chrome
            # options.add_argument('--headless=new')  # Definindo opcoes para rodar a automação web em segundo plano.
            prefs = {"download.default_directory": f"{vgb.dir_gdis}"}  # Definindo o diretorio do Download de arquivos
            options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Desabilitando a captura padrao de bluetooth do navegador
            options.add_experimental_option("prefs", prefs)  # Adicionando as preferencias para Download de arquivos
            service = ChromeService(log_path=f'{vgb.drivers_dir}{vgb.barra}chromedriver.log')  # executable_path=ChromeDriverManager(path=vgb.drivers_dir).install())  # Construindo o servico, download e instalacao do driver automaticamente
            if sys.platform.startswith('win32'):
                service.creation_flags = CREATE_NO_WINDOW  # CREATE_NO_WINDOW desativa a abertura do terminal para download do driver
            self.driver = webdriver.Chrome(options=options, service=service)  # Passando o webdriver para a classe servico e inicializando e realizando o download automatico chrome
            self.inicio_acessa_minhanexx()  # Chamando funcao
    except Exception as erro:
        print('Erro ao inicializar o navegador.')

def inicio_acessa_megasena(self):
    self.driver.maximize_window()  # Definindo para abrir no formato maximizado
    self.driver.get(site1)
    time.sleep(10)
    sys.exit()










# Criar funcao para realizar a busca pelos numeros sorteados.

# Criar funcao para encaminhar palpites de jogos com base nos numeros que mais se repetiram

# Criar funcao para encaminhar por whatsapp
