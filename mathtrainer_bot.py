from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import keyboard  

# Configuração do navegador
navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get('https://mathtrainer.ai/')
time.sleep(5)

# Função para inserir o nome de usuário
def inserir_nome_usuario(nome):
    try:
        campo_nome = navegador.find_element(By.XPATH, '//*[@id="name"]')
        campo_nome.click()
        campo_nome.clear()  
        campo_nome.send_keys(nome)
    except Exception as e:
        print(f"Erro ao inserir nome de usuário: {e}")

# Função para clicar no botão inicial
def clicar_botao_inicial():
    try:
        button = navegador.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/nav')
        if button.is_displayed():
            button.click()
    except Exception as e:
        print(f"Erro ao clicar no botão inicial: {e}")

# Função para resolver problemas matemáticos
def resolver_problemas():
    try:
        while True:
            mathDashboards = navegador.find_elements(By.XPATH, '//*[@id="app"]/div/section')
            if mathDashboards and mathDashboards[0].is_displayed():
                time.sleep(0.5)
                conta_element = navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/section/div/div/span/span/span/span[2]')
                conta_text = conta_element.text.replace('−', '-').replace('×', '*').replace('÷', '/')
                print("Conta identificada:", conta_text)
                resposta = str(eval(conta_text))
                time.sleep(0.1)
                body = navegador.find_element(By.TAG_NAME, 'body')
                body.send_keys(resposta)
            else:
                break
    except Exception as e:
        print(f"Erro ao resolver a conta: {e}")

# Função principal para jogar
def jogar(nome_usuario):
    try:
        inserir_nome_usuario(nome_usuario)
        
        dashboard = navegador.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div')
        dashboardInicial = navegador.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div')

        if dashboard.is_displayed() or dashboardInicial.is_displayed():
            clicar_botao_inicial()
        else:
            resolver_problemas()
    except Exception as e:
        print(f"Erro ao jogar: {e}")

# Loop principal do jogo
try:
    nome_usuario = "SeuNome"
    
    while True:
        jogar(nome_usuario)
        
        if keyboard.is_pressed('F9'):
            print("Script encerrado pelo usuário.")
            break

finally:
    navegador.quit()
