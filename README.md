# Automação em Selenium - Unieuro 

Este é um script de automação desenvolvido em **Python** com a biblioteca **Selenium**. O objetivo principal é automatizar o processo de login na plataforma EAD do Unieuro, navegar até um curso específico e realizar o download de um arquivo PDF.

O script será configurado para rodar no **Google Chrome** no ambiente Windows.

## Funcionalidades

* **Login automático:** Acessa a plataforma EAD com as credenciais fornecidas.
* **Navegação:** Encontra e acessa um curso específico na página "Meus cursos".
* **Download de Arquivo:** Localiza o link de um arquivo PDF (globo.pdf) dentro do curso, captura sua URL e o baixa para uma pasta local.
* **Organização:** Salva o arquivo baixado em uma pasta `downloads` criada na raiz do projeto.

## Pré-requisitos

* **Python 3.8+**
* Navegador **Google Chrome** (Você precisará baixar o **ChromeDriver** correspondente à sua versão do Chrome).

## Instalação e Configuração

Siga os passos abaixo para preparar o ambiente e executar o script no **Windows**.

### 1. Preparação Inicial

* **Clone o repositório** (ou copie os arquivos)
    ```bash
    git clone <url-do-seu-repositorio>
    cd <nome-do-repositorio>
    ```

* **(Opcional, mas recomendado) Crie um ambiente virtual**
    ```bash
    python -m venv venv
    ```

* **Ative o ambiente virtual (Comando para Windows)**
    ```bash
    .\venv\Scripts\activate
    ```

### 2. Instale as Dependências

Crie um arquivo `requirements.txt` com o conteúdo abaixo e instale-as:
selenium
python-dotenv
requests


```bash
pip install -r requirements.txt

Configure o ChromeDriver
Você precisará baixar o driver correto e configurar o caminho no seu código Python:

Baixe o chromedriver.exe na página oficial do ChromeDriver (escolha a versão que corresponde ao seu Google Chrome).

Coloque o arquivo chromedriver.exe em um local conhecido no seu computador.

Importante: No seu script Python (main.py), você precisará definir o caminho completo para este arquivo (ex: CAMINHO_DRIVER = r'C:\Caminho\Para\chromedriver.exe').

Configure as Variáveis de Ambiente
Crie um arquivo chamado .env na pasta do projeto e adicione suas credenciais de acesso:

substitua nas linha onde está escrito:
UNIEURO_USUARIO="esse vai ser usuario"
UNIEURO_SENHA="aqui fica a senha"
