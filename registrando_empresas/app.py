from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl 
from time import sleep

# 1 - fazer login
driver = webdriver.Chrome()
driver.get('https://contabilidade-devaprender.netlify.app')
sleep(3)

# click adicionando
email = driver.find_element(By.XPATH, "//input[@id='email']")
sleep(1)
email.send_keys("admin@contabilidade.com")

# 2 - adicio na senha
senha = driver.find_element(By.XPATH, "//input[@id='senha']")
sleep(1)
senha.send_keys("123456")

botao_entra = driver.find_element(By.XPATH, "//button[@id='Entrar']")
botao_entra.click()

# extrair informação da planilha
empresas = openpyxl.load_workbook("./empresas.xlsx")
pagina_empresas = empresas['dados empresas']

for linha in pagina_empresas.iter_rows(min_row=2, values_only=True):
    nome_empresa, email_empresa, telefone, endereco, cnpj, area_atuacao, quantidade_de_funcionario, data_fundacao = linha

    # Usar WebDriverWait para aguardar até que o elemento esteja disponível
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nomeEmpresa')))
    driver.find_element(By.ID, 'nomeEmpresa').send_keys(nome_empresa)
    sleep(1)
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'emailEmpresa')))
    driver.find_element(By.ID, 'emailEmpresa').send_keys(email_empresa)
    sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'telefoneEmpresa')))
    driver.find_element(By.ID, 'telefoneEmpresa').send_keys(telefone)
    sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'enderecoEmpresa')))
    driver.find_element(By.ID, 'enderecoEmpresa').send_keys(endereco)
    sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'cnpj')))
    driver.find_element(By.ID, 'cnpj').send_keys(cnpj)
    sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'areaAtuacao')))
    driver.find_element(By.ID, 'areaAtuacao').send_keys(area_atuacao)
    sleep(2)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'numeroFuncionarios')))
    driver.find_element(By.ID, 'numeroFuncionarios').send_keys(quantidade_de_funcionario)
    sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dataFundacao')))
    sleep(1)
    driver.find_element(By.ID, 'dataFundacao').send_keys(data_fundacao)
    sleep(1)
    driver.find_element(By.ID,"Cadastrar").click()
    sleep(1)