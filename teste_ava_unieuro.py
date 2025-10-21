from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

USUARIO = "sua_matricula"
SENHA = "sua_senha"
URL_AVA = "http://ead.unieuro.edu.br/" 
NOME_DISCIPLINA = "Projetos"
NOME_ARQUIVO = "globo.pdf"   
PATH_CHROME_DRIVER = None 

def executar_teste():
    driver = None
    try:
        if PATH_CHROME_DRIVER:
            service = ChromeService(executable_path=PATH_CHROME_DRIVER)
            driver = webdriver.Chrome(service=service)
        else:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        print("Iniciando o teste...")
        driver.maximize_window()
        driver.get(URL_AVA)
        wait = WebDriverWait(driver, 20) 

        print("1. Tentando fazer login...")

        campo_usuario = wait.until(EC.presence_of_element_located((By.ID, "username"))) 
        campo_usuario.send_keys(USUARIO)

        campo_senha = driver.find_element(By.ID, "password") 
        campo_senha.send_keys(SENHA)

        botao_login = driver.find_element(By.ID, "loginbtn") 
        botao_login.click()
        
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.dashboard-content")))
        print("   Login bem-sucedido.")

        print(f"2. Buscando a disciplina: '{NOME_DISCIPLINA}'")
        
        try:
            link_disciplina = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, NOME_DISCIPLINA)))
            link_disciplina.click()
            print(f"   Acessando a disciplina '{NOME_DISCIPLINA}'.")
            
            wait.until(EC.title_contains(NOME_DISCIPLINA))
            
        except TimeoutException:
            print(f"ERRO: Não foi possível encontrar ou clicar na disciplina '{NOME_DISCIPLINA}'. Verifique o nome e o seletor.")
            return

        print(f"3. Buscando o arquivo: '{NOME_ARQUIVO}'")

        xpath_arquivo = f"//a[contains(text(), '{NOME_ARQUIVO}')]"

        try:
            link_arquivo = wait.until(EC.presence_of_element_located((By.XPATH, xpath_arquivo)))
            print(f"   SUCESSO: O arquivo '{NOME_ARQUIVO}' foi ENCONTRADO!")
            
            url_download = link_arquivo.get_attribute("href")
            print(f"   URL de Download: {url_download}")
            
        except TimeoutException:
            print(f"   FALHA: O arquivo '{NOME_ARQUIVO}' NÃO foi encontrado na página da disciplina.")
            
    except NoSuchElementException as e:
        print(f"ERRO DE ELEMENTO: Um elemento crucial não foi encontrado. Detalhes: {e}")
    except TimeoutException:
        print("ERRO DE TEMPO LIMITE: A página demorou muito para carregar ou um elemento não apareceu.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        
    finally:
        if driver:
            print("Encerrando o navegador em 5 segundos...")
            time.sleep(5) 
            driver.quit()
        print("Teste finalizado.")

if __name__ == "__main__":
    executar_teste()
