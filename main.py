import os
import time
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# --- 1. CARREGAR VARIÁVEIS DE AMBIENTE DO ARQUIVO .ENV ---
load_dotenv()

# --- 2. CONFIGURAÇÕES INICIAIS ---
USUARIO = os.getenv("UNIEURO_USUARIO")
SENHA = os.getenv("UNIEURO_SENHA")

PASTA_DOWNLOAD = os.path.join(os.getcwd(), "downloads")
if not os.path.exists(PASTA_DOWNLOAD):
    os.makedirs(PASTA_DOWNLOAD)

if not USUARIO or not SENHA:
    print("ERRO: As variáveis UNIEURO_USUARIO e UNIEURO_SENHA não foram encontradas no arquivo .env")
    exit()

# --- 3. CONFIGURAÇÃO DO NAVEGADOR (AJUSTADO PARA CHROME NO WINDOWS) ---

# ⚠️ PASSO CRÍTICO: VOCÊ PRECISA SUBSTITUIR ESTA STRING
# COLE O CAMINHO COMPLETO DO SEU CHROMEDRIVER.EXE AQUI
CAMINHO_DRIVER = "COLE O CAMINHO DO SEU CHROMEDRIVER.EXE AQUI" 

try:
    # Configurações do serviço
    service = Service(CAMINHO_DRIVER)
    
    # Configurações de opções (podemos deixar vazio, mas é necessário para o Service)
    chrome_options = Options()

    navegador = webdriver.Chrome(service=service, options=chrome_options)
    navegador.maximize_window()
    wait = WebDriverWait(navegador, 20)

    print(">>> Iniciando automação com o Chrome no Windows...")

    # --- PASSOS A, B, C (Acesso e Login) ---
    print(">>> Acessando o site ead.unieuro.edu.br...")
    navegador.get("https://ead.unieuro.edu.br/")
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Acessar"))).click()

    print(">>> Preenchendo usuário e senha...")
    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(USUARIO)
    navegador.find_element(By.ID, "password").send_keys(SENHA)
    navegador.find_element(By.ID, "loginbtn").click()

    # --- PASSO D: ACESSAR O CURSO ---
    print(">>> Aguardando o carregamento da página 'Meus cursos'...")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Meus cursos']")))
    
    print(">>> Login realizado com sucesso! Procurando o curso...")
    nome_exato_do_curso = "24 | GPSINN | PROJETO INTEGRADOR DE SISTEMAS COMPUTACIONAIS"
    curso = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(., '{nome_exato_do_curso}')]")))
    
    print(f">>> Curso '{nome_exato_do_curso}' encontrado! Acessando...")
    curso.click()

    # --- PASSO E: ENCONTRAR E ABRIR O PDF ---
    wait.until(EC.visibility_of_element_located((By.ID, "page-header")))
    print(">>> Página do curso carregada. Procurando o link do arquivo 'globo.pdf'...")
    
    arquivo_pdf_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'globo.pdf')]/ancestor::a")))
    
    print(">>> Link encontrado! Navegando para a página do PDF...")
    arquivo_pdf_link.click()

    # --- PASSO F: CAPTURAR A URL E BAIXAR ---
    print(">>> Aguardando o carregamento do PDF na aba atual...")
    # Uma pausa é útil para garantir que a URL seja atualizada
    time.sleep(5) 
    
    pdf_url = navegador.current_url
    print(f">>> URL do PDF encontrada: {pdf_url}")

    # Usa a biblioteca requests para baixar o arquivo
    print(">>> Baixando o arquivo diretamente da URL...")
    
    # É CRÍTICO: Se a URL do PDF exige login, pode ser necessário passar os cookies de sessão 
    # do Selenium para o 'requests'. Para simplificar, mantive a chamada original, 
    # mas esteja ciente desse possível ponto de falha se o download der erro 403/401.
    
    response = requests.get(pdf_url)
    
    if response.status_code == 200:
        caminho_salvar = os.path.join(PASTA_DOWNLOAD, "globo.pdf")
        
        with open(caminho_salvar, "wb") as f:
            f.write(response.content)
        print(f">>> Arquivo salvo com sucesso em: {caminho_salvar}")
    else:
        print(f">>> ERRO: Não foi possível baixar o arquivo. Status: {response.status_code}")
    
    print(">>> PROCESSO FINALIZADO COM SUCESSO! <<<")

finally:
    # --- FECHAR O NAVEGADOR ---
    print(">>> Fechando o navegador.")
    if 'navegador' in locals() and navegador:
        navegador.quit()
