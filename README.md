# Automação em Selenium 

Este é um script de automação desenvolvido em **Python** com a biblioteca **Selenium**. O objetivo principal é automatizar o processo de login na plataforma AVA (Ambiente Virtual de Aprendizagem) do Unieuro, navegar até a disciplina de "Projetos" e verificar a existência do arquivo `globo.pdf`.

O script é configurado para rodar no **Google Chrome** e utiliza o `webdriver-manager` para gerenciar automaticamente o **ChromeDriver**, simplificando a configuração inicial.

## Funcionalidades

* **Login automático:** Acessa a plataforma AVA com as credenciais fornecidas.
* **Navegação:** Encontra e acessa a disciplina **"Projetos"** na página de cursos.
* **Verificação de Arquivo:** Localiza o link do arquivo **`globo.pdf`** dentro da disciplina e reporta se ele foi encontrado, exibindo sua URL.
* **Execução Simples:** Utiliza o `webdriver-manager` para instalar e gerenciar o driver do navegador, dispensando a configuração manual do caminho (`chromedriver.exe`).

## Pré-requisitos

Para executar este projeto, você precisa ter apenas o **Python** instalado em seu sistema.

* **Python 3.8+**
* Navegador **Google Chrome** (deve estar instalado, o driver é gerenciado automaticamente).

## Instalação e Configuração

Siga os passos abaixo para preparar o ambiente e executar o script.

### 1. Preparação Inicial

Clone o repositório (ou copie os arquivos) para sua máquina:

```bash
git clone <url-do-seu-repositorio>
cd <nome-do-repositorio>
````

**(Opcional, mas Altamente Recomendado) Crie e ative um ambiente virtual:**

```bash
# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Windows)
.\venv\Scripts\activate

# Ativa o ambiente virtual (Linux/macOS)
source venv/bin/activate
```

### 2\. Instale as Dependências

Crie um arquivo `requirements.txt` com o conteúdo abaixo e instale as bibliotecas necessárias.

**Conteúdo de `requirements.txt`:**

```
selenium
webdriver-manager
```

**Instalação:**

```bash
pip install -r requirements.txt
```

### 3\. Configure as Variáveis de Acesso

Embora o script fornecido use variáveis internas, para aderir a uma boa prática (e a sua sugestão de `python-dotenv`), **recomenda-se** configurar suas credenciais em um arquivo `.env` para maior segurança.

Crie um arquivo chamado **`.env`** na pasta raiz do projeto e adicione suas credenciais:

```
# .env file
UNIEURO_USUARIO="sua_matricula"
UNIEURO_SENHA="sua_senha_secreta"
```

> **Atenção:** Você precisará adaptar o script Python (`teste_ava_unieuro.py`) para ler essas variáveis usando a biblioteca `python-dotenv` se desejar usar o `.env`.

### 4\. Execução do Script

Com as dependências instaladas e o script devidamente configurado com as suas credenciais e seletores (`By.ID`, `By.XPATH`, etc.) corretos para o AVA do Unieuro, execute o teste com o seguinte comando:

```bash
python teste_ava_unieuro.py
